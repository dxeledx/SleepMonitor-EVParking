# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_primary = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_primary.sizePolicy().hasHeightForWidth())
        self.label_primary.setSizePolicy(sizePolicy)
        self.label_primary.setText("")
        self.label_primary.setObjectName("label_primary")
        self.horizontalLayout.addWidget(self.label_primary)
        self.label_result = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.horizontalLayout.addWidget(self.label_result)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_15.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbtn_detect_sleeping = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtn_detect_sleeping.sizePolicy().hasHeightForWidth())
        self.rbtn_detect_sleeping.setSizePolicy(sizePolicy)
        self.rbtn_detect_sleeping.setStyleSheet("font: 20pt \"等线\";")
        self.rbtn_detect_sleeping.setChecked(True)
        self.rbtn_detect_sleeping.setObjectName("rbtn_detect_sleeping")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtn_detect_sleeping)
        self.horizontalLayout_2.addWidget(self.rbtn_detect_sleeping)
        self.rbtn_detect_polygon = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtn_detect_polygon.sizePolicy().hasHeightForWidth())
        self.rbtn_detect_polygon.setSizePolicy(sizePolicy)
        self.rbtn_detect_polygon.setStyleSheet("font: 20pt \"等线\";")
        self.rbtn_detect_polygon.setObjectName("rbtn_detect_polygon")
        self.buttonGroup.addButton(self.rbtn_detect_polygon)
        self.horizontalLayout_2.addWidget(self.rbtn_detect_polygon)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_detect_sleeping = QtWidgets.QWidget()
        self.page_detect_sleeping.setStyleSheet("font: 11pt \"等线\";")
        self.page_detect_sleeping.setObjectName("page_detect_sleeping")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_detect_sleeping)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_detect_sleeping = QtWidgets.QFormLayout()
        self.formLayout_detect_sleeping.setObjectName("formLayout_detect_sleeping")
        self.Label = QtWidgets.QLabel(self.page_detect_sleeping)
        self.Label.setStyleSheet("font: 16pt \"等线\"")
        self.Label.setObjectName("Label")
        self.formLayout_detect_sleeping.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.lineEdit_cur_model1 = QtWidgets.QLineEdit(self.page_detect_sleeping)
        self.lineEdit_cur_model1.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_cur_model1.setObjectName("lineEdit_cur_model1")
        self.formLayout_detect_sleeping.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_cur_model1)
        self.line_2 = QtWidgets.QFrame(self.page_detect_sleeping)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_detect_sleeping.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.Label_3 = QtWidgets.QLabel(self.page_detect_sleeping)
        self.Label_3.setStyleSheet("font: 16pt \"等线\"")
        self.Label_3.setObjectName("Label_3")
        self.formLayout_detect_sleeping.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.lineEdit_inputfolder1 = QtWidgets.QLineEdit(self.page_detect_sleeping)
        self.lineEdit_inputfolder1.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_inputfolder1.setObjectName("lineEdit_inputfolder1")
        self.formLayout_detect_sleeping.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inputfolder1)
        self.line_3 = QtWidgets.QFrame(self.page_detect_sleeping)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout_detect_sleeping.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.Label_4 = QtWidgets.QLabel(self.page_detect_sleeping)
        self.Label_4.setStyleSheet("font: 16pt \"等线\"")
        self.Label_4.setObjectName("Label_4")
        self.formLayout_detect_sleeping.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.lineEdit_outputfolder1 = QtWidgets.QLineEdit(self.page_detect_sleeping)
        self.lineEdit_outputfolder1.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_outputfolder1.setObjectName("lineEdit_outputfolder1")
        self.formLayout_detect_sleeping.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_outputfolder1)
        self.line_4 = QtWidgets.QFrame(self.page_detect_sleeping)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout_detect_sleeping.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.label_9 = QtWidgets.QLabel(self.page_detect_sleeping)
        self.label_9.setStyleSheet("font: 16pt \"等线\"")
        self.label_9.setObjectName("label_9")
        self.formLayout_detect_sleeping.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.gridLayout_3.addLayout(self.formLayout_detect_sleeping, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_detect_sleeping)
        self.page_detect_polygon = QtWidgets.QWidget()
        self.page_detect_polygon.setObjectName("page_detect_polygon")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_detect_polygon)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_detect_polygon = QtWidgets.QFormLayout()
        self.formLayout_detect_polygon.setObjectName("formLayout_detect_polygon")
        self.Label_2 = QtWidgets.QLabel(self.page_detect_polygon)
        self.Label_2.setStyleSheet("font: 16pt \"等线\"")
        self.Label_2.setObjectName("Label_2")
        self.formLayout_detect_polygon.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.lineEdit_cur_model2 = QtWidgets.QLineEdit(self.page_detect_polygon)
        self.lineEdit_cur_model2.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_cur_model2.setObjectName("lineEdit_cur_model2")
        self.formLayout_detect_polygon.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_cur_model2)
        self.Label_5 = QtWidgets.QLabel(self.page_detect_polygon)
        self.Label_5.setStyleSheet("font: 16pt \"等线\"")
        self.Label_5.setObjectName("Label_5")
        self.formLayout_detect_polygon.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.lineEdit_inputfolder2 = QtWidgets.QLineEdit(self.page_detect_polygon)
        self.lineEdit_inputfolder2.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_inputfolder2.setObjectName("lineEdit_inputfolder2")
        self.formLayout_detect_polygon.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inputfolder2)
        self.Label_6 = QtWidgets.QLabel(self.page_detect_polygon)
        self.Label_6.setStyleSheet("font: 16pt \"等线\"")
        self.Label_6.setObjectName("Label_6")
        self.formLayout_detect_polygon.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.lineEdit_outputfolder2 = QtWidgets.QLineEdit(self.page_detect_polygon)
        self.lineEdit_outputfolder2.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_outputfolder2.setObjectName("lineEdit_outputfolder2")
        self.formLayout_detect_polygon.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_outputfolder2)
        self.Label_7 = QtWidgets.QLabel(self.page_detect_polygon)
        self.Label_7.setStyleSheet("font: 16pt \"等线\"")
        self.Label_7.setObjectName("Label_7")
        self.formLayout_detect_polygon.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.lineEdit_standard_parking_count = QtWidgets.QLineEdit(self.page_detect_polygon)
        self.lineEdit_standard_parking_count.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_standard_parking_count.setObjectName("lineEdit_standard_parking_count")
        self.formLayout_detect_polygon.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_standard_parking_count)
        self.Label_8 = QtWidgets.QLabel(self.page_detect_polygon)
        self.Label_8.setStyleSheet("font: 16pt \"等线\"")
        self.Label_8.setObjectName("Label_8")
        self.formLayout_detect_polygon.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.lineEdit_illegal_parking_count = QtWidgets.QLineEdit(self.page_detect_polygon)
        self.lineEdit_illegal_parking_count.setStyleSheet("font: 16pt \"等线\"")
        self.lineEdit_illegal_parking_count.setObjectName("lineEdit_illegal_parking_count")
        self.formLayout_detect_polygon.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_illegal_parking_count)
        self.Label_9 = QtWidgets.QLabel(self.page_detect_polygon)
        self.Label_9.setStyleSheet("font: 16pt \"等线\"")
        self.Label_9.setObjectName("Label_9")
        self.formLayout_detect_polygon.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.chkbox_open_userdefined_paint = QtWidgets.QCheckBox(self.page_detect_polygon)
        self.chkbox_open_userdefined_paint.setMinimumSize(QtCore.QSize(10, 10))
        self.chkbox_open_userdefined_paint.setIconSize(QtCore.QSize(20, 20))
        self.chkbox_open_userdefined_paint.setObjectName("chkbox_open_userdefined_paint")
        self.formLayout_detect_polygon.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.chkbox_open_userdefined_paint)
        self.line_6 = QtWidgets.QFrame(self.page_detect_polygon)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayout_detect_polygon.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line_6)
        self.line_7 = QtWidgets.QFrame(self.page_detect_polygon)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.formLayout_detect_polygon.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_7)
        self.line_8 = QtWidgets.QFrame(self.page_detect_polygon)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.formLayout_detect_polygon.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_8)
        self.line_9 = QtWidgets.QFrame(self.page_detect_polygon)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.formLayout_detect_polygon.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.line_9)
        self.line_10 = QtWidgets.QFrame(self.page_detect_polygon)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.formLayout_detect_polygon.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.line_10)
        self.gridLayout_2.addLayout(self.formLayout_detect_polygon, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_detect_polygon)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("font: 16pt \"等线\"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textLog = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textLog.setObjectName("textLog")
        self.verticalLayout.addWidget(self.textLog)
        self.btn_empty_textLog = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_empty_textLog.setStyleSheet("font: 16pt \"等线\"")
        self.btn_empty_textLog.setObjectName("btn_empty_textLog")
        self.verticalLayout.addWidget(self.btn_empty_textLog)
        self.verticalLayout_10.addWidget(self.groupBox_2)
        self.verticalLayout_10.setStretch(0, 3)
        self.verticalLayout_10.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.horizontalLayout_4.setStretch(0, 5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_13.addWidget(self.line_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet("font: 16pt \"等线\"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cbBox_modelinfor = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbBox_modelinfor.sizePolicy().hasHeightForWidth())
        self.cbBox_modelinfor.setSizePolicy(sizePolicy)
        self.cbBox_modelinfor.setObjectName("cbBox_modelinfor")
        self.horizontalLayout_3.addWidget(self.cbBox_modelinfor)
        self.tbtn_selectmodel = QtWidgets.QToolButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbtn_selectmodel.sizePolicy().hasHeightForWidth())
        self.tbtn_selectmodel.setSizePolicy(sizePolicy)
        self.tbtn_selectmodel.setObjectName("tbtn_selectmodel")
        self.horizontalLayout_3.addWidget(self.tbtn_selectmodel)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line_14 = QtWidgets.QFrame(self.groupBox_3)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_4.addWidget(self.line_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_photo = QtWidgets.QWidget()
        self.tab_photo.setObjectName("tab_photo")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_photo)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.tab_photo)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.lineEidt_photo = QtWidgets.QLineEdit(self.tab_photo)
        self.lineEidt_photo.setObjectName("lineEidt_photo")
        self.horizontalLayout_10.addWidget(self.lineEidt_photo)
        self.tbtn_selectphoto = QtWidgets.QToolButton(self.tab_photo)
        self.tbtn_selectphoto.setObjectName("tbtn_selectphoto")
        self.horizontalLayout_10.addWidget(self.tbtn_selectphoto)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.tab_photo, "")
        self.tab_video = QtWidgets.QWidget()
        self.tab_video.setObjectName("tab_video")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_video)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.tab_video)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.lineEdit_video = QtWidgets.QLineEdit(self.tab_video)
        self.lineEdit_video.setObjectName("lineEdit_video")
        self.horizontalLayout_9.addWidget(self.lineEdit_video)
        self.tbtn_selectvideo = QtWidgets.QToolButton(self.tab_video)
        self.tbtn_selectvideo.setObjectName("tbtn_selectvideo")
        self.horizontalLayout_9.addWidget(self.tbtn_selectvideo)
        self.tabWidget.addTab(self.tab_video, "")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_camera)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_initcamera = QtWidgets.QPushButton(self.tab_camera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_initcamera.sizePolicy().hasHeightForWidth())
        self.btn_initcamera.setSizePolicy(sizePolicy)
        self.btn_initcamera.setObjectName("btn_initcamera")
        self.horizontalLayout_16.addWidget(self.btn_initcamera)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cbBox_selectcamara = QtWidgets.QComboBox(self.tab_camera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbBox_selectcamara.sizePolicy().hasHeightForWidth())
        self.cbBox_selectcamara.setSizePolicy(sizePolicy)
        self.cbBox_selectcamara.setObjectName("cbBox_selectcamara")
        self.horizontalLayout_11.addWidget(self.cbBox_selectcamara)
        self.btn_selectcamera = QtWidgets.QPushButton(self.tab_camera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_selectcamera.sizePolicy().hasHeightForWidth())
        self.btn_selectcamera.setSizePolicy(sizePolicy)
        self.btn_selectcamera.setObjectName("btn_selectcamera")
        self.horizontalLayout_11.addWidget(self.btn_selectcamera)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 3)
        self.horizontalLayout_12.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_camera, "")
        self.horizontalLayout_18.addWidget(self.tabWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_13.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setStyleSheet("font: 16pt \"等线\"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.HSlider_Conf = QtWidgets.QSlider(self.groupBox_4)
        self.HSlider_Conf.setProperty("value", 60)
        self.HSlider_Conf.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_Conf.setObjectName("HSlider_Conf")
        self.horizontalLayout_5.addWidget(self.HSlider_Conf)
        self.dspinBox_conf = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.dspinBox_conf.setMaximum(1.0)
        self.dspinBox_conf.setSingleStep(0.05)
        self.dspinBox_conf.setObjectName("dspinBox_conf")
        self.horizontalLayout_5.addWidget(self.dspinBox_conf)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.line_11 = QtWidgets.QFrame(self.groupBox_4)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_5.addWidget(self.line_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.HSlider_Iou = QtWidgets.QSlider(self.groupBox_4)
        self.HSlider_Iou.setProperty("value", 50)
        self.HSlider_Iou.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_Iou.setObjectName("HSlider_Iou")
        self.horizontalLayout_6.addWidget(self.HSlider_Iou)
        self.dspinBox_Iou = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.dspinBox_Iou.setMaximum(1.0)
        self.dspinBox_Iou.setSingleStep(0.05)
        self.dspinBox_Iou.setObjectName("dspinBox_Iou")
        self.horizontalLayout_6.addWidget(self.dspinBox_Iou)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.line_12 = QtWidgets.QFrame(self.groupBox_4)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_5.addWidget(self.line_12)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_17.addWidget(self.label_5)
        self.HSlider_linewidth = QtWidgets.QSlider(self.groupBox_4)
        self.HSlider_linewidth.setMinimum(0)
        self.HSlider_linewidth.setMaximum(99)
        self.HSlider_linewidth.setProperty("value", 10)
        self.HSlider_linewidth.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_linewidth.setTickInterval(0)
        self.HSlider_linewidth.setObjectName("HSlider_linewidth")
        self.horizontalLayout_17.addWidget(self.HSlider_linewidth)
        self.spinbox_linewidth = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinbox_linewidth.setMaximum(10)
        self.spinbox_linewidth.setProperty("value", 1)
        self.spinbox_linewidth.setObjectName("spinbox_linewidth")
        self.horizontalLayout_17.addWidget(self.spinbox_linewidth)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_13.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setStyleSheet("font: 16pt \"等线\"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rbtn_nosave = QtWidgets.QRadioButton(self.groupBox_5)
        self.rbtn_nosave.setStyleSheet("font: 16pt \"等线\"")
        self.rbtn_nosave.setChecked(True)
        self.rbtn_nosave.setObjectName("rbtn_nosave")
        self.verticalLayout_3.addWidget(self.rbtn_nosave)
        self.rbtn_autosave = QtWidgets.QRadioButton(self.groupBox_5)
        self.rbtn_autosave.setStyleSheet("font: 16pt \"等线\"")
        self.rbtn_autosave.setChecked(False)
        self.rbtn_autosave.setObjectName("rbtn_autosave")
        self.verticalLayout_3.addWidget(self.rbtn_autosave)
        self.rbtn_selectsave = QtWidgets.QRadioButton(self.groupBox_5)
        self.rbtn_selectsave.setStyleSheet("font: 16pt \"等线\"")
        self.rbtn_selectsave.setObjectName("rbtn_selectsave")
        self.verticalLayout_3.addWidget(self.rbtn_selectsave)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setStyleSheet("font: 16pt \"等线\"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_save = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_save.setObjectName("lineEdit_save")
        self.horizontalLayout_7.addWidget(self.lineEdit_save)
        self.tbtn_save = QtWidgets.QToolButton(self.groupBox_5)
        self.tbtn_save.setStyleSheet("font: 16pt \"等线\"")
        self.tbtn_save.setObjectName("tbtn_save")
        self.horizontalLayout_7.addWidget(self.tbtn_save)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_start = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setStyleSheet("font: 16pt \"等线\"")
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_6.addWidget(self.btn_start)
        self.btn_pause = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy)
        self.btn_pause.setStyleSheet("font: 16pt \"等线\"")
        self.btn_pause.setObjectName("btn_pause")
        self.verticalLayout_6.addWidget(self.btn_pause)
        self.btn_termination = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_termination.sizePolicy().hasHeightForWidth())
        self.btn_termination.setSizePolicy(sizePolicy)
        self.btn_termination.setStyleSheet("font: 16pt \"等线\"")
        self.btn_termination.setObjectName("btn_termination")
        self.verticalLayout_6.addWidget(self.btn_termination)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.line = QtWidgets.QFrame(self.groupBox_5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_clear_polygon = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear_polygon.sizePolicy().hasHeightForWidth())
        self.btn_clear_polygon.setSizePolicy(sizePolicy)
        self.btn_clear_polygon.setStyleSheet("font: 16pt \"等线\"")
        self.btn_clear_polygon.setObjectName("btn_clear_polygon")
        self.verticalLayout_14.addWidget(self.btn_clear_polygon)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.groupBox_5)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_4.addWidget(self.line_13, 2, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.groupBox_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.verticalLayout_13.setStretch(0, 3)
        self.verticalLayout_13.setStretch(2, 1)
        self.gridLayout.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "视频输出"))
        self.rbtn_detect_sleeping.setText(_translate("MainWindow", "检测1"))
        self.rbtn_detect_polygon.setText(_translate("MainWindow", "检测2"))
        self.Label.setText(_translate("MainWindow", "当前模型"))
        self.Label_3.setText(_translate("MainWindow", "输入路径"))
        self.Label_4.setText(_translate("MainWindow", "输出路径"))
        self.label_9.setText(_translate("MainWindow", "ID与计时"))
        self.Label_2.setText(_translate("MainWindow", "当前模型"))
        self.Label_5.setText(_translate("MainWindow", "输入路径"))
        self.Label_6.setText(_translate("MainWindow", "输出路径"))
        self.Label_7.setText(_translate("MainWindow", "规范停车计数"))
        self.Label_8.setText(_translate("MainWindow", "违规停车计数"))
        self.Label_9.setText(_translate("MainWindow", "开启变色绘图"))
        self.groupBox_2.setTitle(_translate("MainWindow", "信息输出"))
        self.btn_empty_textLog.setText(_translate("MainWindow", "清空"))
        self.groupBox_3.setTitle(_translate("MainWindow", "选择区"))
        self.label_2.setText(_translate("MainWindow", "输入来源"))
        self.label.setText(_translate("MainWindow", "权重文件："))
        self.tbtn_selectmodel.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "选择路径："))
        self.tbtn_selectphoto.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_photo), _translate("MainWindow", "🖼️ 照片"))
        self.label_4.setText(_translate("MainWindow", "选择路径："))
        self.tbtn_selectvideo.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_video), _translate("MainWindow", "🎞️ 视频"))
        self.btn_initcamera.setText(_translate("MainWindow", "初始化摄像头"))
        self.btn_selectcamera.setText(_translate("MainWindow", "选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), _translate("MainWindow", "📷 摄像头"))
        self.groupBox_4.setTitle(_translate("MainWindow", "参数调整"))
        self.label_6.setText(_translate("MainWindow", "Conf"))
        self.label_7.setText(_translate("MainWindow", "Iou"))
        self.label_5.setText(_translate("MainWindow", "linewidth"))
        self.groupBox_5.setTitle(_translate("MainWindow", "操作区"))
        self.rbtn_nosave.setText(_translate("MainWindow", "不保存"))
        self.rbtn_autosave.setText(_translate("MainWindow", "自动保存"))
        self.rbtn_selectsave.setText(_translate("MainWindow", "选择保存"))
        self.label_8.setText(_translate("MainWindow", "保存路径："))
        self.tbtn_save.setText(_translate("MainWindow", "..."))
        self.btn_start.setText(_translate("MainWindow", "✅ 开始"))
        self.btn_pause.setText(_translate("MainWindow", "⛔ 暂停"))
        self.btn_termination.setText(_translate("MainWindow", "🔴 终止"))
        self.btn_clear_polygon.setText(_translate("MainWindow", "清除所有顶点"))