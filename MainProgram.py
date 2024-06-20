import sys
import PyQt5
import cv2, os, time, datetime
import pygame

from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTextBrowser, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from UIProgram.MainUI import Ui_MainWindow

from ultralytics import YOLO

from threading import Thread



# 可拖动绘制多边形的 QLabel 子类
class PolygonLabel(QtWidgets.QLabel):
    polygonChanged = QtCore.pyqtSignal(QtGui.QPolygonF)  # 信号，通知多边形发生了变化

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.polygon = QtGui.QPolygonF()  # 存储多边形的顶点
        self.current_point = None  # 当前正在移动的顶点
        self.is_drawing = False  # 绘制标记
        self.polygon_coords = []  # 初始化存储顶点坐标的列表

    def mousePressEvent(self, event):
        pos = self.clamp_point(event.pos())  # 将点击位置约束在 QLabel 内
        if event.button() == QtCore.Qt.LeftButton:
            if self.is_near_existing_point(pos):  # 检查是否靠近已存在的顶点
                self.current_point = self.get_closest_point(pos)  # 获取最近的顶点
            else:  # 否则添加新的顶点
                self.polygon.append(QtCore.QPointF(pos))
                self.polygonChanged.emit(self.polygon)  # 发出信号，通知多边形已改变
            self.update()  # 更新界面
        elif event.button() == QtCore.Qt.RightButton:
            pos = event.pos()
            if self.is_near_existing_point(pos):
                closest_point = self.get_closest_point(pos)
                try:
                    # 找到顶点的索引
                    index = self.polygon.indexOf(closest_point)
                    # 根据索引删除顶点
                    self.polygon.remove(index)
                    self.polygonChanged.emit(self.polygon)  # 发出信号
                    self.update()  # 更新界面
                except Exception as e:
                    print("Error during right-click deletion:", e)  # 捕获异常并输出

    def mouseMoveEvent(self, event):
        if self.current_point:  # 如果正在移动顶点
            new_pos = self.clamp_point(event.pos())  # 约束到 QLabel 内
            index = self.polygon.indexOf(self.current_point)  # 获取当前顶点的索引
            if index != -1:  # 确保索引有效
                self.polygon.replace(index, QtCore.QPointF(new_pos))  # 更新位置
                self.update()  # 更新界面

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:  # 左键松开
            if self.current_point is not None:
                self.polygonChanged.emit(self.polygon)  # 发出信号
            self.current_point = None  # 重置当前顶点

    def paintEvent(self, event):
        super().paintEvent(event)  # 保持父类功能
        if not self.polygon.isEmpty():  # 如果多边形不为空
            painter = QtGui.QPainter(self)  # 创建画笔
            pen = QtGui.QPen(QtCore.Qt.blue, 2)  # 设置绘制线条的笔
            painter.setPen(pen)
            painter.drawPolyline(self.polygon)  # 绘制多边形
            if len(self.polygon) > 2:  # 如果多边形有多个顶点
                painter.drawLine(self.polygon[-1], self.polygon[0])  # 闭合多边形

    def is_near_existing_point(self, pos, tolerance=10):
        """检查给定位置是否靠近已有顶点"""
        return any((pos - point).manhattanLength() < tolerance for point in self.polygon)

    def get_closest_point(self, pos):
        """返回最接近的位置"""
        return min(self.polygon, key=lambda point: (pos - point).manhattanLength())

    def update_polygon(self, new_polygon):
        """更新多边形"""
        self.polygon = QtGui.QPolygonF(new_polygon)
        self.update()  # 更新界面

    # 当多边形变化时，更新其顶点列表
    def on_polygon_changed(self, polygon):
        if polygon.isEmpty():
            return  # 如果多边形为空，什么都不做
        self.polygon_coords = [(point.x(), point.y()) for point in polygon]
        print(self.polygon_coords)

    def get_polygon_coords(self):
        # 获取多边形的顶点坐标
        return [(point.x(), point.y()) for point in self.polygon]

    # 重置多边形，清除所有顶点
    def clear_polygon(self):
        self.polygon.clear()  # 清空多边形的所有顶点
        self.update()  # 触发重绘以清除界面上的多边形
        self.polygonChanged.emit(self.polygon)  # 发送信号通知多边形已被重置

    # 确保顶点在 QLabel 内部
    def clamp_point(self, point):
        """将给定的点约束在 QLabel 的边界之内"""
        width = self.width() - 1
        height = self.height() - 1
        clamped_x = max(0, min(point.x(), width))  # 将 x 约束在 0 和 width 之间
        clamped_y = max(0, min(point.y(), height))  # 将 y 约束在 0 和 height 之间
        return QtCore.QPointF(clamped_x, clamped_y)  # 返回约束后的点



# 自定义信号源对象
class MySignals(QObject):

    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串----
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    # type QTextBrowser
    text_print_signal = pyqtSignal(QTextBrowser,str)

    # 还可以定义其他种类的信号
    update_table = pyqtSignal(str)

    # 新的信号，用于更新 QLabel
    update_label_signal = pyqtSignal(int, float)  # 接收两个参数，track_id 和持续时间

    def get_polygon(self):
        return self.polygon_item.polygon()



class MyGui(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__initUI__()
        self.__initFlag__()
        self.__initSignal__()

        self.label_map = {}  # 存储 track_id 和 QLabel 的映射


        #polygon 变化信号槽
        self.label_primary.polygonChanged.connect(self.on_polygon_changed)
        self.label_result.polygonChanged.connect(self.on_polygon_changed)

        # 初始化计时器字典和最后检测时间字典
        self.track_times = {}
        self.last_detection_times = {}


        # 定义定时器  视频定时器
        self.timer_video = QtCore.QTimer()
        # 定时到le
        self.timer_video.timeout.connect(self.show_video)

        # 摄像头定时器
        self.timer_camera = QtCore.QTimer()
        # 定时到le
        self.timer_camera.timeout.connect(self.show_camera)

        # 要处理的视频帧图片队列，目前就放1帧图片
        self.frameToAnalyze = []

        #按键监听
        self.lisener()

        # 启动时以全屏模式显示
        self.showMaximized()


    def __initUI__(self):
        self.setWindowTitle("安徽工业大学校园规范监督系统")
        self.setWindowIcon(QIcon("./UIProgram/img/AHUT1.png"))


        #参数区
        self.dspinBox_conf.setValue(0.60)   # conf默认显示值
        self.dspinBox_Iou.setValue(0.50)  # iou默认显示值
        self.spinbox_linewidth.setValue(1)  #line_width默认显示值
        self.HSlider_linewidth.setValue(10)
        self.spinbox_linewidth.setMaximum(10)
        self.dspinBox_Iou.setMaximum(1)
        self.dspinBox_conf.setMaximum(1)

        #stackWidget默认值
        self.stackedWidget.setCurrentIndex(0)

        #添加按键组
        self.save_btn_group = QtWidgets.QButtonGroup()
        self.save_btn_group.addButton(self.rbtn_nosave)
        self.save_btn_group.addButton(self.rbtn_autosave)
        self.save_btn_group.addButton(self.rbtn_selectsave)

        #保存不可按
        self.tbtn_save.setDisabled(True)


        # 移除旧的 QLabel
        self.horizontalLayout.removeWidget(self.label_primary)
        self.horizontalLayout.removeWidget(self.label_result)

        # 将现有的 QLabel 替换为 RectLabel
        self.label_primary = PolygonLabel()
        self.label_result = PolygonLabel()

        # 同步矩形框
        self.label_primary.polygonChanged.connect(self.label_result.update_polygon)
        self.label_result.polygonChanged.connect(self.label_primary.update_polygon)

        # 将 RectLabel 添加到原有布局
        self.horizontalLayout.addWidget(self.label_primary)
        self.horizontalLayout.addWidget(self.label_result)

        self.label_primary.setStyleSheet('border:1px solid #D7E2F9;')
        self.label_result.setStyleSheet('border:1px solid #D7E2F9;')

        self.label_primary.setScaledContents(True)
        self.label_result.setScaledContents(True)

        self.label_primary.setMinimumSize(798,690)
        self.label_result.setMinimumSize(798, 690)
        self.label_primary.setMaximumSize(798, 690)
        self.label_result.setMaximumSize(798, 690)

        #设置不可写
        self.lineEdit_cur_model1.setReadOnly(True)
        self.lineEdit_cur_model2.setReadOnly(True)
        self.lineEdit_inputfolder1.setReadOnly(True)
        self.lineEdit_inputfolder2.setReadOnly(True)
        self.lineEdit_outputfolder1.setReadOnly(True)
        self.lineEdit_outputfolder2.setReadOnly(True)
        self.lineEdit_standard_parking_count.setReadOnly(True)
        self.lineEdit_illegal_parking_count.setReadOnly(True)


    def __initFlag__(self):
        #是否允许关闭窗口
        self.allow_windowshutdown = True
        #线程结束标志
        self.stop_Thread_flag = False
        #model是否加载标志
        self.model_selected_flag = False

        #开始按钮是否点击标志
        self.start_btn_clicked_flag = False
        #暂停按钮是否点击标志
        self.pause_btn_clicked_flag = False
        #结束按钮是否点击标识
        self.stop_btn_clicked_flag = False

        #图片是否已选择标志
        self.image_selected_flag = False
        #视频是否已选择
        self.video_selected_flag = False
        #摄像头是否已打开
        self.camera_opened_flag = False

        # 初始化pygame
        pygame.init()


        # 参数区
        self.image = ''
        self.camera = ''
        self.cap = ''
        self.sleep_warn_audio_folder = "./resource/audio/检测到睡觉.mp3"
        self.bicycle_warn_audio_folder = "./resource/audio/检测到违规停放，请规范停放车辆.mp3"
        self.audio_is_playing = False
        # sleep检测相关参数
        self.sleeping_target_count = 0  # id总数
        self.sleeping_target_labels = {}
        #违停检测相关参数
        self.y_position_ratio = 0.2


        # 保存与否
        self.save_value = 'nosave'
        self.output_folder = 'D:/yolov8/ultralytics-main/result_save/'
        #文件名
        self.file_name = ''
        self.video_writer = None

        #检测相关参数
        self.linewidth = 1
        self.conf_value = 0.6
        self.iou_value = 0.5

        self.previous_tab_index = self.tabWidget.currentIndex()

        #是否采用自定义绘图来实现红绿变色
        self.open_userdefined_paint_Flag = False

        # 检测模式 0 sleeping  1 car
        self.detect_mode_Flag = 0

        self.paint_mode_Flag = 0

    def __initSignal__(self):
        #实例化 MySignal 对象
        self.printSignal = MySignals()
        self.signals = MySignals()  # 创建自定义信号实例

    def printToGui(self,wid,info):
        wid.append(info)

    def lisener(self):
        #加载模型
        self.tbtn_selectmodel.clicked.connect(self.select_model)
        #模型改变
        self.cbBox_modelinfor.currentIndexChanged.connect(self.selected_model_change)

        #tab变化检测
        self.tabWidget.currentChanged.connect(self.tab_changed)

        #照片文件
        self.tbtn_selectphoto.clicked.connect(self.open_image)

        #视频文件
        self.tbtn_selectvideo.clicked.connect(self.open_video)

        #摄像头
        self.btn_initcamera.clicked.connect(self.init_camera)
        self.btn_selectcamera.clicked.connect(self.select_camera)

        #conf,iou,line_width滑块
        self.HSlider_Conf.valueChanged.connect(self.conf_Hslider_value_changed)
        self.dspinBox_conf.valueChanged[float].connect(self.conf_dspinbox_value_changed)

        self.HSlider_Iou.valueChanged.connect(self.iou_slider_value_changed)
        self.dspinBox_Iou.valueChanged[float].connect(self.iou_spinbox_value_changed)

        self.HSlider_linewidth.valueChanged.connect(self.line_width_slider_value_changed)
        self.spinbox_linewidth.valueChanged.connect(self.line_width_spinbox_value_changed)

        #保存
        self.save_btn_group.buttonClicked.connect(self.whether_to_save)
        self.tbtn_save.clicked.connect(self.selectOutputFolder)


        #开始 暂停 终止
        self.btn_start.clicked.connect(self.start)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_termination.clicked.connect(self.stop)

        # 自定义信号区 连接信号到更新 textLog 的槽
        self.printSignal.text_print_signal.connect(self.printToGui)
        # 将信号连接到槽函数
        self.signals.update_label_signal.connect(self.update_label_in_formlayout)

        # 清空textLog
        self.btn_empty_textLog.clicked.connect(self.empty_textLog)
        #清空polygon
        self.btn_clear_polygon.clicked.connect(self.empty_polygon)

        #检测sleeping或者car选择
        self.rbtn_detect_sleeping.toggled.connect(self.on_rbtn_detect_toggled)

    #选择模型
    def select_model(self):
        defaultDir = "D:/yolov8/ultralytics-main/models"
        filenames, _ = QFileDialog.getOpenFileNames(
            self, "选择权重", defaultDir, ".pt (*.pt)")
        if not filenames:
            QMessageBox.warning(self,"警告","打开权重文件失败")
            return()

        # 遍历选中的文件，检查是否已存在
        for filename in filenames:
            filename_onlyname = Path(filename).name
            # 检查是否重复
            if self.cbBox_modelinfor.findText(filename_onlyname) == -1:
                self.cbBox_modelinfor.addItem(f"{filename_onlyname}", filename)

        #设置显示为新添加的model
        self.cbBox_modelinfor.setCurrentIndex(self.cbBox_modelinfor.count() - 1)
        self.model = YOLO(filename)
        #self.model = YOLO("./ultralytics/cfg/models/v8/yolov8.yaml")
        QMessageBox.information(self,"成功","权重加载成功")
        self.lineEdit_cur_model1.setText(Path(filename).name)
        self.lineEdit_cur_model2.setText(Path(filename).name)
        self.model_selected_flag = True

    #模型改变
    def selected_model_change(self):
        index = self.cbBox_modelinfor.currentIndex()
        self.model = YOLO(self.cbBox_modelinfor.itemData(index))
        self.lineEdit_cur_model1.setText(self.cbBox_modelinfor.currentText())
        self.lineEdit_cur_model2.setText(self.cbBox_modelinfor.currentText())

    #重写resizeEvent方法
    def resizeEvent(self,event):
        # 获取新的窗口大小
        new_size = event.size()
        if new_size.width() == 1618 and new_size.height() == 895:
            self.label_primary.setMaximumSize(644, 537)
            self.label_result.setMaximumSize(649, 534)
        elif new_size.width() == 1920 and new_size.height() == 1040:
            self.label_primary.setMaximumSize(812, 700)
            self.label_result.setMaximumSize(812, 700)
        else:
            self.label_primary.setMaximumSize(16777215, 16777215)
            self.label_result.setMaximumSize(16777215, 16777215)

        # 确保父类的 resizeEvent 被调用
        super().resizeEvent(event)

    # 重写 closeEvent 方法
    def closeEvent(self, event):
        #未关闭子线程不允许关闭窗口
        if not self.allow_windowshutdown:
            event.ignore() #阻止关闭
            QMessageBox.warning(self,"警告","请先终止线程后再关闭窗口！")
        #若资源未释放，则释放
        if self.cap and self.cap.isOpened():
            self.cap.release()
        if self.camera and self.camera.isOpened():
            self.camera.release()
        #super().closeEvent(event)

    #检测模式选择
    def on_rbtn_detect_toggled(self):
        if self.rbtn_detect_sleeping.isChecked():
            self.stackedWidget.setCurrentIndex(0)
            self.detect_mode_Flag = 0
            self.chkbox_open_userdefined_paint.setChecked(False)
        if self.rbtn_detect_polygon.isChecked():
            self.stackedWidget.setCurrentIndex(1)
            self.detect_mode_Flag = 1

    def tab_changed(self):
        if self.start_btn_clicked_flag and not self.stop_btn_clicked_flag:
            QMessageBox.warning(self, "警告", "请先终止再切换")
            self.tabWidget.blockSignals(True)  # 暂时阻止信号，防止循环
            self.tabWidget.setCurrentIndex(self.previous_tab_index)
            self.tabWidget.blockSignals(False)  # 恢复信号
        else:
            self.previous_tab_index = self.tabWidget.currentIndex()

        self.rbtn_nosave.setChecked(True)
        self.lineEdit_save.clear()

    #打开图片
    def open_image(self):
        defaultDir = "D:/yolov8/ultralytics-main/resource/images"
        options = QFileDialog.Options()  # 创建文件对话框选项
        filename, _ = QFileDialog.getOpenFileName(
            self, "选择图片", defaultDir, "Images (*.png *.jpg *.jpeg)", options=options
        )

        if filename:
            self.file_name = filename
            self.image_selected_flag = True

            #路径显示
            self.lineEidt_photo.setText(filename)
            self.lineEdit_inputfolder1.setText(filename)
            self.lineEdit_inputfolder2.setText(filename)

            # 读取图像
            image = cv2.imread(filename)  # OpenCV 默认读取 BGR 格式
            self.image = cv2.imread(filename)
            #设置大小
            self.image = cv2.resize(self.image,(640,480))
            image = cv2.resize(image, (640, 480))
            # 转换为 RGB 格式
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # 创建 QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            qImage = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # 设置 QLabel
            pixmap = QPixmap.fromImage(qImage)

            # 适当缩放但保持比例
            scaled_pixmap = pixmap.scaled(
                self.label_primary.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )

            # 设置 QLabel 显示图像
            self.label_primary.setPixmap(scaled_pixmap)

            # 铺满label
            self.label_result.setScaledContents(True)

            # #铺满label
            # self.label_primary.setScaledContents(True)

    #图片检测子线程
    def detectPhotoThreadFunc(self):
        frame = self.image  # 使用 OpenCV 原始数据
        #转化成RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #设置图片大小解决坐标参考不统一问题
        frame = cv2.resize(frame,(self.label_primary.width(),self.label_primary.height()))


        # 开始计时
        start_time = time.time()
        # 开始检测
        results = self.model.track(frame, conf = self.conf_value, iou = self.iou_value )[0]#classes = [0]
        boxes = results.boxes
        # 结束计时
        end_time = time.time()

        # 计算检测所需时间
        detection_time = (end_time - start_time) * 1000  # 毫秒
        output_info = (f"信息: {results.verbose()} 用时: {int(detection_time)}ms")  # 位置: {results.boxes.xyxy}

        self.printSignal.text_print_signal.emit(self.textLog, output_info)

        polygon_coords = self.label_primary.get_polygon_coords()

        # 如果是检测计时模式
        if not self.detect_mode_Flag:
            # 检测计时
            self.target_timing(boxes)
        else:
            # 判断是否在polygon内
            self.out_of_polygon_process(boxes)

        # 是否采用自定义绘图实现变色功能
        if self.chkbox_open_userdefined_paint.isChecked():
            img = self.draw_custom_boxes(frame.copy(), boxes, polygon_coords)
        else:
            img = results.plot(line_width=self.linewidth)

        # 如果没有检测到框，输出信息,并显示原图像
        if not boxes or len(boxes) == 0:
            self.printSignal.text_print_signal.emit(self.textLog, "No targets detected")
            img = frame  # 退出函数



        # 确保颜色转换正确
        if img is not None:
            height, width, _ = img.shape
            bytes_per_line = 3 * width

            # 创建 QImage 并转换为 RGB 格式
            qImage = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap_result = QPixmap.fromImage(qImage)

            self.label_result.setPixmap(pixmap_result)


        if self.save_value != "nosave":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            file_extension = self.file_name.split('.')[-1]
            new_filename = now + '.' + file_extension  # 获得文件后缀名
            file_path = self.output_folder + 'img_output/' + new_filename
            print(file_path)
            cv2.imwrite(file_path, img)

    #打开视频
    def open_video(self):
        defaultDir = "D:/yolov8/ultralytics-main/resource/video"
        filename, _ = QFileDialog.getOpenFileName(
            self, "打开视频", defaultDir, "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
        if filename:
            self.lineEdit_video.setText(filename)
            self.lineEdit_inputfolder1.setText(filename)
            self.lineEdit_inputfolder2.setText(filename)

            self.video_selected_flag = True
            self.cap = cv2.VideoCapture(filename)

            self.show_video()
        else:
            QMessageBox.warning(self, "错误", "未选择视频文件")

    def show_video(self):
        ret, frame = self.cap.read()
        if not ret:
            QMessageBox.information(self, "提示", "视频播放完毕或无法读取视频帧")
            if self.video_writer:
                self.video_writer.release()  # 释放资源
                self.video_writer = None
            self.timer_video.stop()
            return
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (self.label_primary.width(), self.label_primary.height()))


        height, width, channels = frame.shape
        bytes_per_line = channels * width
        qImage = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        pixmap = QtGui.QPixmap.fromImage(qImage)
        self.label_primary.setPixmap(pixmap)

        #如果队列为空，则入队一帧
        if not self.frameToAnalyze:
            self.frameToAnalyze.append(frame)

    #视频检测子线程
    def detectVideoThreadFunc(self):
        while not self.stop_Thread_flag:
            # 如果没来得及生产，则等待
            if not self.frameToAnalyze:
                time.sleep(0.01)
                continue

            frame = self.frameToAnalyze.pop(0)

            # 开始计时
            start_time = time.time()
            #开始检测
            results = self.model.track(frame, conf = self.conf_value, iou = self.iou_value)[0]
            # 结束计时
            end_time = time.time()

            boxes = results.boxes  # 获取检测到的框


            # 计算检测所需时间
            detection_time = (end_time - start_time) * 1000  # 毫秒
            output_info = (f"信息: {results.verbose()} 用时: {int(detection_time)}ms")  #位置: {results.boxes.xyxy}
            self.printSignal.text_print_signal.emit(self.textLog,output_info)


            polygon_coords = self.label_primary.get_polygon_coords()

            # 如果是检测计时模式
            if not self.detect_mode_Flag:
                # 检测计时
                self.target_timing(boxes)
            else:
                # 判断是否在polygon内
                self.out_of_polygon_process(boxes)

            # 是否采用自定义绘图实现变色功能
            if self.chkbox_open_userdefined_paint.isChecked():
                # 自定义绘图
                img = self.draw_custom_boxes(frame.copy(), boxes, polygon_coords)
            else:
                img = results.plot(line_width=self.linewidth)

            bytes_per_line = img.shape[1] * img.shape[2]  # 宽度 * 通道数
            qImage = QtGui.QImage(img.data, img.shape[1], img.shape[0], bytes_per_line,
                                  QtGui.QImage.Format_RGB888)

            self.label_result.setPixmap(QtGui.QPixmap.fromImage(qImage))  # 往显示Label里 显示QImage

            self.result_save(img) # 保存结果

            time.sleep(0.1)

    def init_camera(self):
        QMessageBox.information(self,"正在检测","正在检测摄像头")
        total = 0
        cap = cv2.VideoCapture()  # 视频流对象
        index = 3
        while index >= 0:
            ret = cap.open(index)
            if ret:
                total += 1
                cap.release()
            index -= 1
        if total > 0:
            count = f"检测成功，共有{total}个摄像头"
            QMessageBox.information(self,"成功",count)
            #添加下拉框
            for i in range(total):
                capindex = f"摄像头{i}"
                self.cbBox_selectcamara.addItem(capindex)

    def select_camera(self):
        index = self.cbBox_selectcamara.currentIndex()
        self.camera = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        # 错误检测
        if not self.camera.isOpened():
            str = f"摄像头{index}打开失败！"
            QMessageBox.warning(self, "失败", str)
            return ()

        self.camera_opened_flag = True

        #显示信息
        self.lineEdit_inputfolder1.setText(self.cbBox_selectcamara.currentText())
        self.lineEdit_inputfolder2.setText(self.cbBox_selectcamara.currentText())

        if self.timer_camera.isActive() == False:  # 若定时器未启动
            self.timer_camera.start(30)

    def show_camera(self):
        ret, frame = self.camera.read()  # 从视频流中读取
        if not ret:
            return()
            # 视频色彩转换回RGB，OpenCV images as BGR

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (self.label_primary.width(), self.label_primary.height()))

        height, width, channels = frame.shape
        bytes_per_line = channels * width
        qImage = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        pixmap = QtGui.QPixmap.fromImage(qImage)
        self.label_primary.setPixmap(pixmap)

        # 如果队列为空，则入队一帧
        if not self.frameToAnalyze:
            self.frameToAnalyze.append(frame)

    #子线程
    #摄像头检测子线程
    def frameAnalyzeThreadFunc(self):

        while not self.stop_Thread_flag:
            #如果没来得及生产，则等待
            if not self.frameToAnalyze:
                time.sleep(0.01)
                continue

            frame = self.frameToAnalyze.pop(0)

            # 开始计时
            start_time = time.time()
            # 开始检测
            results = self.model.track(frame, conf=self.conf_value, iou=self.iou_value)[0]
            # 结束计时
            end_time = time.time()

            boxes = results.boxes  # 获取检测到的框

            # 计算检测所需时间
            detection_time = (end_time - start_time) * 1000  # 毫秒
            output_info = (f"信息: {results.verbose()} 用时: {int(detection_time)}ms")  # 位置: {results.boxes.xyxy}
            self.printSignal.text_print_signal.emit(self.textLog, output_info)

            polygon_coords = self.label_primary.get_polygon_coords()

            # 如果是检测计时模式
            if not self.detect_mode_Flag:
                # 检测计时
                self.target_timing(boxes)
            else:
                # 判断是否在polygon内
                self.out_of_polygon_process(boxes)

            # 是否采用自定义绘图实现变色功能
            if self.chkbox_open_userdefined_paint.isChecked():
                # 自定义绘图
                img = self.draw_custom_boxes(frame.copy(), boxes, polygon_coords)
            else:
                img = results.plot(line_width=self.linewidth)

            bytes_per_line = img.shape[1] * img.shape[2]  # 宽度 * 通道数
            qImage = QtGui.QImage(img.data, img.shape[1], img.shape[0], bytes_per_line,
                                  QtGui.QImage.Format_RGB888)

            self.label_result.setPixmap(QtGui.QPixmap.fromImage(qImage))  # 往显示Label里 显示QImage

            time.sleep(0.1)

    #清空textLog
    def empty_textLog(self):
        self.textLog.clear()

    #清空polygon
    def empty_polygon(self):
        self.label_primary.clear_polygon()
        self.label_result.clear_polygon()

    #conf slider改变
    def conf_Hslider_value_changed(self, value):
        # 将滑动条的值（0-100）转换为浮点值（0.0-1.0）
        float_value = value / 100.0
        self.conf_value = float_value
        # 阻止信号发送以避免循环，更新值，然后取消阻止
        self.dspinBox_conf.blockSignals(True)
        self.dspinBox_conf.setValue(float_value)
        self.dspinBox_conf.blockSignals(False)

    #conf spinBox改变
    def conf_dspinbox_value_changed(self,value):
        # 将双精度旋转框的值（0.0-1.0）转换为滑动条的值（0-100）
        slider_value = int(value * 100)
        self.conf_value = value
        # 阻止信号发送以避免循环，更新值，然后取消阻止
        self.HSlider_Conf.blockSignals(True)
        self.HSlider_Conf.setValue(slider_value)
        self.HSlider_Conf.blockSignals(False)

    def iou_slider_value_changed(self, value):
        float_value = value / 100.0
        self.iou_value = float_value
        self.dspinBox_Iou.blockSignals(True)
        self.dspinBox_Iou.setValue(float_value)
        self.dspinBox_Iou.blockSignals(False)

    def iou_spinbox_value_changed(self, value):
        slider_value = int(value * 100)
        self.iou_value = value
        self.HSlider_Iou.blockSignals(True)
        self.HSlider_Iou.setValue(slider_value)
        self.HSlider_Iou.blockSignals(False)

    def line_width_slider_value_changed(self, value):
        int_value = int(value / 10)
        self.linewidth = int_value
        self.spinbox_linewidth.blockSignals(True)
        self.spinbox_linewidth.setValue(int_value)
        self.spinbox_linewidth.blockSignals(False)

    def line_width_spinbox_value_changed(self, value):
        slider_value = int(value * 10)
        self.linewidth = slider_value
        self.HSlider_linewidth.blockSignals(True)
        self.HSlider_linewidth.setValue(slider_value)
        self.HSlider_linewidth.blockSignals(False)

    #设置保存
    def whether_to_save(self,button):
        if button == self.rbtn_autosave:
            self.save_value = 'autosave'
            self.tbtn_save.setDisabled(True)
            self.output_folder = 'D:/yolov8/ultralytics-main/result_save/'
            self.lineEdit_save.setText(self.output_folder)
            self.lineEdit_outputfolder1.setText(self.output_folder)
            self.lineEdit_outputfolder2.setText(self.output_folder)
        elif button == self.rbtn_selectsave:
            self.lineEdit_save.setText(self.output_folder)
            self.save_value = 'selectsave'
            self.tbtn_save.setDisabled(False)
            self.output_folder = self.lineEdit_save.text()
            self.lineEdit_save.clear()
            self.lineEdit_outputfolder1.clear()
            self.lineEdit_outputfolder2.clear()
        else:
            self.save_value = 'nosave'
            self.tbtn_save.setDisabled(True)
            self.lineEdit_save.clear()
            self.lineEdit_outputfolder1.clear()
            self.lineEdit_outputfolder2.clear()

    def selectOutputFolder(self):
        # 弹出文件夹选择对话框
        folder = QFileDialog.getExistingDirectory(self, "选择保存路径")
        if folder:
            # 设置输出文件夹
            self.output_folder = folder
            # 显示所选路径
            self.lineEdit_save.setText(self.output_folder)
            self.lineEdit_outputfolder1.setText(self.output_folder)
            self.lineEdit_outputfolder2.setText(self.output_folder)


    #检测sleeping计时
    def target_timing(self, boxes):
        # 在检测过程中
        if boxes is not None:
            current_time = time.time()
            detected_ids = set()  # 存储此帧中检测到的track_id
            # 遍历所有检测框
            for box in boxes:
                class_index = int(box.cls.item())  # 获取类别索引
                if class_index in self.model.names:
                    obj_class = self.model.names[class_index]
                else:
                    obj_class = "unknown"  # 如果无效

                track_id = int(box.id.item())  # 获取目标的跟踪 ID
                detected_ids.add(track_id)  # 添加到检测集合中

                if obj_class == "sleeping":  # 检查是否为 "sleeping" 类
                    if track_id not in self.track_times or track_id not in self.last_detection_times or current_time - \
                            self.last_detection_times[track_id] > 1:
                        # 重新开始计时
                        self.track_times[track_id] = current_time

                    # 更新最后检测时间
                    self.last_detection_times[track_id] = current_time

                    # 计算持续时间
                    duration = current_time - self.track_times[track_id]
                    # 发射信号，让 GUI 线程更新对应的 QLabel
                    self.signals.update_label_signal.emit(track_id, duration)

                    if duration > 5:
                        Thread(target=self.play_audio_Func, kwargs={"audio": self.sleep_warn_audio_folder}).start()


            # 检查未在此帧中检测到的跟踪目标
            missing_ids = set(self.track_times.keys()) - detected_ids
            for track_id in missing_ids:
                if current_time - self.last_detection_times[track_id] > 1:
                    # 移除超过1秒未检测到的目标的计时器
                    del self.track_times[track_id]
                    del self.last_detection_times[track_id]

                    # 从 layout 中删除对应的 QLabel
                    if track_id in self.label_map:
                        label = self.label_map.pop(track_id)
                        self.formLayout_detect_sleeping.removeRow(label)


    # GUI 线程中的槽函数，用于更新 QLabel
    def update_label_in_formlayout(self, track_id, duration):
        if track_id not in self.label_map:
            # 如果是第一次创建这个 label，将它添加到 formLayout_detect_sleeping
            new_label = QtWidgets.QLabel()
            self.formLayout_detect_sleeping.addRow(f"目标 {track_id} 持续时间:", new_label)
            self.label_map[track_id] = new_label

        # 更新 QLabel 的文本内容
        label = self.label_map[track_id]
        label.setText(f"{duration:.2f} 秒")


    #播放警报
    def play_audio_Func(self,audio):
        if not self.audio_is_playing:  # 检查是否有音频正在播放
            self.audio_is_playing = True  # 标记开始播放
            print("开始播放音频")
            pygame.mixer.music.load(audio)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            self.audio_is_playing = False  # 音频播放完成，重置标志位
            print("音频播放结束")
        else:
            print("音频正在播放中，跳过本次播放")


    def on_polygon_changed(self, polygon):
        # 接收 polygonChanged 信号，提取坐标
        polygon_coords = [(point.x(), point.y()) for point in polygon]


    # 射线法判断点是否在多边形内  返回 is_inside 的真假
    def is_point_in_polygon(self, point, polygon):
        if len(polygon) < 3:
            return False  # 如果多边形顶点少于3个，则不可能形成封闭多边形
        px, py = point
        is_inside = False
        n = len(polygon)

        j = n - 1
        for i in range(n):
            p1x, p1y = polygon[j]
            p2x, p2y = polygon[i]

            # 判断点与多边形边的交点数
            if (
                    (p1y > py) != (p2y > py)
                    and (px < (p2x - p1x) * (py - p1y) / (p2y - p1y) + p1x)
            ):
                is_inside = not is_inside
            j = i

        return is_inside

    # 实现 box in boxex 的计数
    def out_of_polygon_process(self,boxes):
        #计数
        count_inside = 0
        count_outside = 0

        # 获取多边形顶点坐标
        polygon_coords = self.label_primary.get_polygon_coords()

        for box in boxes:
            xyxy = box.xyxy[0]
            # 根据比例计算y轴的位置
            y_pos = xyxy[1] + (1 - self.y_position_ratio) * (xyxy[3] - xyxy[1])

            # 中心点
            center_point = ((xyxy[0] + xyxy[2]) / 2, y_pos)

            # 判断是否在多边形内
            if self.is_point_in_polygon(center_point, polygon_coords):
                count_inside += 1
            else:
                count_outside += 1

        self.lineEdit_standard_parking_count.setText(f"{count_inside}")
        self.lineEdit_illegal_parking_count.setText(f"{count_outside}")

    # 处理检测框，改变颜色，用画的框覆盖原来的
    def process_boxes(self, img, boxes, polygon_coords):
        for box in boxes:
            xyxy = box.xyxy[0]
            # 根据比例计算y轴的位置
            y_pos = xyxy[1] + (1 - self.y_position_ratio) * (xyxy[3] - xyxy[1])

            # 中心点
            center_point = ((xyxy[0] + xyxy[2]) / 2, y_pos)

            color = (0, 255, 0)  # 绿色，默认在多边形内
            if not self.is_point_in_polygon(center_point, polygon_coords):
                color = (255, 0, 0)  # 红色，表示在多边形外

            # 绘制矩形框
            start_point = (int(xyxy[0]), int(xyxy[1]))
            end_point = (int(xyxy[2]), int(xyxy[3]))
            cv2.rectangle(img, start_point, end_point, color, self.linewidth + 2)

    # 结果自定义画框，在polygon内绿色，在polygon外红色
    def draw_custom_boxes(self, img, boxes, polygon_coords):
        font = cv2.FONT_HERSHEY_SIMPLEX  # 使用OpenCV的Hershey-Simplex字体
        font_scale = 0.5  # 字体大小
        thickness = 2  # 绘制线条的粗细

        # 检查是否有检测框
        if not int(boxes[0].id.item()):
            return img  # 如果没有检测框，返回原始图像，不做任何处理

        for box in boxes:
            xyxy = box.xyxy[0]  # 获取检测框的四个坐标 [x1, y1, x2, y2]
            label = self.model.names[int(box.cls.item())]  # 获取目标类别名称
            confidence = box.conf.item() if hasattr(box, "conf") else None  # 获取置信度
            obj_id = int(box.id.item()) if hasattr(box, "id") else None  # 获取目标ID

            # 根据比例计算y轴的位置
            y_pos = xyxy[1] + (1 - self.y_position_ratio) * (xyxy[3] - xyxy[1])

            # 中心点
            center_point = ((xyxy[0] + xyxy[2]) / 2, y_pos)


            # 使用射线法判断中心点是否在多边形内
            if self.is_point_in_polygon(center_point, polygon_coords):
                color = (0, 255, 0)  # 绿色，用于表示在多边形内
            else:
                color = (255, 0, 0)  # 红色，用于表示在多边形外

            # 在图像上绘制检测框
            cv2.rectangle(
                img,
                (int(xyxy[0]), int(xyxy[1])),  # 左上角坐标
                (int(xyxy[2]), int(xyxy[3])),  # 右下角坐标
                color,  # 矩形框的颜色
                thickness,  # 线条粗细
            )

            # 创建包含类别、ID、置信度的标签文本
            if confidence is not None:
                label_text = f"ID:{obj_id if obj_id else 'N/A'} {label} {confidence:.2f}"
            else:
                label_text = f"ID:{obj_id if obj_id else 'N/A'} {label})"

            # 为文本添加背景矩形
            text_size, _ = cv2.getTextSize(label_text, font, font_scale, thickness)  # 获取文本尺寸
            text_width, text_height = text_size  # 文本的宽度和高度

            # 在框的顶部绘制一个矩形背景以显示文本
            cv2.rectangle(
                img,
                (int(xyxy[0]), int(xyxy[1]) - text_height),  # 背景矩形的左上角
                (int(xyxy[0]) + text_width, int(xyxy[1])),  # 背景矩形的右下角
                color,  # 背景的颜色
                -1,  # 填充背景
            )

            # 在背景矩形上绘制标签文本
            cv2.putText(
                img,
                label_text,  # 文本内容
                (int(xyxy[0]), int(xyxy[1]) - 3),  # 文本位置
                font,  # 使用的字体
                font_scale,  # 字体大小
                (255, 255, 255),  # 白色字体
                thickness,  # 字体粗细
                cv2.LINE_AA,  # 抗锯齿
            )

        return img

    def result_save(self, img):
        if img is not None:
            # 确保图像是RGB格式
            if img.shape[2] == 3:  # 假定img是彩色图像
                # 转换为BGR用于写入
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 从原视频获取宽度
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 从原视频获取高度
            # 确保图像大小与VideoWriter初始化时的大小一致
            if (img.shape[1], img.shape[0]) != (width, height):
                img = cv2.resize(img, (width, height))

            if self.video_writer:
                self.video_writer.write(img)  # 写入视频帧

    def start(self):
        index = self.tabWidget.currentIndex()
        #未选择权重会闪退 加判断
        if not self.model_selected_flag:
            QMessageBox.warning(self,"错误","权重文件未加载，请先加载权重文件!")
            return()

        #避免重复开始
        if self.start_btn_clicked_flag:
            QMessageBox.warning(self,"警告","请勿重复开始")
            return

        #图片子线程
        if index == 0:
            if not self.image_selected_flag:
                QMessageBox.warning(self,"警告","照片文件未选择，请先选择照片文件！")
                return()
            #self.start_btn_clicked_flag = True
            self.pause_btn_clicked_flag = False
            self.stop_Thread_flag = False

            Thread(target=self.detectPhotoThreadFunc, daemon=True).start()

        #检测视频子线程
        elif index == 1:
            if not self.video_selected_flag:
                QMessageBox.warning(self,"警告","视频文件未选择，请先选择视频文件！")
                return()
            self.start_btn_clicked_flag = True
            self.pause_btn_clicked_flag = False
            self.stop_Thread_flag = False

            # 检查是否选择保存视频
            if self.save_value in ['autosave', 'selectsave']:
                output_folder = os.path.join(self.output_folder, "video_output")
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)  # 如果文件夹不存在，则创建文件夹

                current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                output_video_path = os.path.join(output_folder, f'{current_time}.mp4')


                fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编解码器
                fps = self.cap.get(cv2.CAP_PROP_FPS)  # 从原视频获取帧率
                width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 从原视频获取宽度
                height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 从原视频获取高度
                self.video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
                if not self.video_writer.isOpened():
                    QMessageBox.warning(self, "错误", "视频写入器初始化失败！请检查编解码器支持。")
                    return

            Thread(target=self.detectVideoThreadFunc, daemon=True).start()
            #打开视频定时器，原始视频开始播放
            if self.timer_video.isActive() == False:  # 若定时器未启动
                #动态加载视频帧率
                fps = self.cap.get(cv2.CAP_PROP_FPS)
                interval = int(1000 / fps)
                self.timer_video.start(interval)
            self.allow_windowshutdown = False


        #检测摄像头，开始检测子线程
        elif index == 2:
            if not self.frameToAnalyze:
                QMessageBox.warning(self,"警告","摄像头未开启，请先开启摄像头")
                return ()
            if not self.camera_opened_flag:
                QMessageBox.warning(self,"警告","摄像头未选择，请先选择摄像头！")
                return()

            self.start_btn_clicked_flag = True
            self.pause_btn_clicked_flag = False
            self.stop_Thread_flag = False

            # 启动处理摄像头视频帧独立线程
            Thread(target=self.frameAnalyzeThreadFunc, daemon=True).start()
            self.allow_windowshutdown = False


        else:
            QMessageBox.warning(self,"错误","错误")

    def pause(self):
        index = self.tabWidget.currentIndex()

        # 避免重复暂停
        if self.pause_btn_clicked_flag:
            QMessageBox.warning(self, "警告", "请勿重复暂停")
            return

        if not self.start_btn_clicked_flag:
            QMessageBox.warning(self,"警告","暂停错误，尚未开始!")
            time.sleep(1)
            return()

        if index == 0:
            QMessageBox.warning(self,"警告","图片无法暂停")
        elif index == 1:
            #开始按钮重新变得可点击
            self.start_btn_clicked_flag = False
            self.pause_btn_clicked_flag = True
            if self.timer_video.isActive():
                self.timer_video.stop()
                print("视频定时器已关闭")
            if not self.stop_Thread_flag:
                self.stop_Thread_flag = True
        elif index == 2:
            # 开始按钮重新变得可点击
            self.start_btn_clicked_flag = False
            self.pause_btn_clicked_flag = True
            if self.timer_camera.isActive():
                self.timer_camera.stop()
                print("摄像头定时器已关闭")
            if not self.stop_Thread_flag:
                self.stop_Thread_flag = True

    def stop(self):
        self.stop_Thread_flag = True
        self.allow_windowshutdown = True

        index = self.tabWidget.currentIndex()

        #未开始就终止会闪退 加判断
        if not self.start_btn_clicked_flag and not self.pause_btn_clicked_flag and not index:
            QMessageBox.warning(self,"警告","终止错误，尚未开始!")
            time.sleep(1)
            return()


        if self.label_primary.pixmap() is not None:  # 清空视频显示区域
            self.label_primary.clear()
        if self.label_result.pixmap() is not None:  # 清空视频显示区域
            self.label_result.clear()
            time.sleep(0.3)
            self.label_result.clear()

        if index == 0:
            self.start_btn_clicked_flag = False  # 重置开始按钮点击信号
            self.stop_btn_clicked_flag = True  # 重置终止按钮点击信号
            self.lineEidt_photo.clear()
            self.file_name = ''

            if self.label_primary.pixmap() is not None:  # 清空视频显示区域
                self.label_primary.clear()
            if self.label_result.pixmap() is not None:  # 清空视频显示区域
                self.label_result.clear()
                time.sleep(0.3)
                self.label_result.clear()

        elif index == 1:
            #将队列处理干净
            if self.frameToAnalyze:
                self.frameToAnalyze.pop(0)

            self.start_btn_clicked_flag = False# 重置开始按钮点击信号
            self.stop_btn_clicked_flag = True  # 重置终止按钮点击信号
            self.lineEdit_video.clear()
            self.file_name = ''

            if self.video_writer:
                self.video_writer.release()  # 释放资源
                self.video_writer = None

            if self.timer_video.isActive():  # 关闭视频定时器
                self.timer_video.stop()


            if self.cap.isOpened():  # 释放视频流
                self.cap.release()

            if self.label_primary.pixmap() is not None:  # 清空视频显示区域
                self.label_primary.clear()
            if self.label_result.pixmap() is not None:  # 清空视频显示区域
                self.label_result.clear()
                time.sleep(0.3)
                self.label_result.clear()

        elif index == 2:
            self.file_name = ''

            # 将队列处理干净
            if self.frameToAnalyze:
                self.frameToAnalyze.pop(0)

            self.start_btn_clicked_flag = False  # 重置开始按钮点击信号
            self.stop_btn_clicked_flag = True  # 重置终止按钮点击信号

            if self.video_writer:
                self.video_writer.release()  # 释放资源
                self.video_writer = None

            if self.timer_camera.isActive():  # 关闭摄像头定时器
                self.timer_camera.stop()
            if self.camera.isOpened():  # 释放视频流
                self.camera.release()

            if self.label_primary.pixmap() is not None:  # 清空视频显示区域
                self.label_primary.clear()
            if self.label_result.pixmap() is not None:  # 清空视频显示区域
                self.label_result.clear()
                time.sleep(0.3)
                self.label_result.clear()



if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MyUIstart = MyGui()
    MyUIstart.show()
    sys.exit(app.exec_())