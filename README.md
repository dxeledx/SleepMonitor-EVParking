# 项目介绍
本项目是本人的本科毕业设计，由 yolov8 + PyQt5 开发。主要可用于睡觉行为的检测和电动车的违停检测（可切换模型实现其他车辆的违停检测）。

## 文件及目录介绍
[models](https://github.com/dxeledx/SleepMonitor-EVParking/tree/main/models)文件夹：存放了<font style="color:rgb(31, 35, 40);">训练好的电瓶车模型 vehicle.pt，和睡觉姿势模型 sleeping.pt。</font>

[UIProgram](https://github.com/dxeledx/SleepMonitor-EVParking/tree/main/UIProgram)文件夹：存放了UI界面源代码，及相关图标的照片。

[ultralytics](https://github.com/dxeledx/SleepMonitor-EVParking/tree/main/ultralytics)文件夹：yolov8相关代码

[video_test](https://github.com/dxeledx/SleepMonitor-EVParking/tree/main/video_test)文件夹：相关测试视频

[MainProgram.py](https://github.com/dxeledx/SleepMonitor-EVParking/blob/main/MainProgram.py)：程序入口与主程序

[yolo_bvn.yaml](https://github.com/dxeledx/SleepMonitor-EVParking/blob/main/yolo_bvn.yaml)：训练模型的参数设置

[yolov8_train.py](https://github.com/dxeledx/SleepMonitor-EVParking/blob/main/yolov8_train.py)：启动训练模型程序入口

[yolov8_val.py](https://github.com/dxeledx/SleepMonitor-EVParking/blob/main/yolov8_val.py)：验证模型精度程序入口

[yolov8n.pt](https://github.com/dxeledx/SleepMonitor-EVParking/blob/main/yolov8n.pt)：yolov8官方模型文件

## 检测机制说明
**1、睡觉检测：**

利用模型识别睡觉姿势，并对每个目标进行标号（利用ByteTrack），随后对其进行计时，如果超过5秒，则发出警报；如果消失1秒以内后重新出现，则继续上次的基础上继续计时；如果消失超过1秒，并再次出现，则重新计时。

**2、违停检测：**

利用模型识别电动车目标，检测其是否在用户自定义的规范停车区域内。

# 运行项目
## 1、配置环境
### 视频教程：
详细配置环境教程视频：[https://www.bilibili.com/video/BV1nm81eYEkZ/](https://www.bilibili.com/video/BV1nm81eYEkZ/)

### 文字教程：
#### 1、安装python
进入python官网（[https://www.python.org/downloads/](https://www.python.org/downloads/)），选择合适自己系统的版本进行安装。

#### 2、安装Anaconda
进入Anaconda官网并下载安装包：[https://www.anaconda.com/download](https://www.anaconda.com/download)

#### 3、<font style="color:rgb(31, 35, 40);">创建conda虚拟环境</font>
打开pycharm中的终端或搜索Anaconda prompt打开，在命令行中输入以下命令，创建一个名字为 yolov8 的conda虚拟环境。可选步骤：指定python版本为3.12

```plain
conda create -n yolov8 python==3.12
```

激活虚拟环境

```plain
conda activate yolov8
```

<font style="color:rgb(31, 35, 40);">配置清华源（修改默认），可以使我们安装包的时候更快</font>

```plain
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 4、安装依赖包
**（1）安装pytorch**

首先需要<font style="color:#DF2A3F;">查看自己的cuda版本</font>（N卡）（<font style="color:#DF2A3F;">重要</font>），然后进入pytorch官网（[https://pytorch.org/](https://pytorch.org/)）选择合适的版本安装。选择合适的命令在终端中执行即可。

**（2）安装yolov8所需包**

在终端中进入项目文件夹（“cd + 盘符号” 切换盘符，“cd + 具体路径” 进入具体路径），然后执行以下命令安装相关依赖。

```plain
pip install -e .
```

**（3）安装其余依赖包**

在终端中执行以下命令安装剩余所需依赖。

```plain
pip install PyQt5 opencv-python pygame
```

## 2、开始运行
运行MainProgram.py即可运行程序。

## 3、使用程序
![](https://cdn.nlark.com/yuque/0/2024/png/50508020/1734587146852-7000a808-f443-4b59-9cae-026549578298.png)

### 界面介绍
中间最大的两个空白框分别显示原始图像与检测后的图像。右侧输出检测相关参数。下方为操作区，分别进行模型和输入源选择、参数调整和控制按钮。

### 开始检测前准备
必须步骤：在开始检测前需要在左下角选择好模型权重文件，以及输入的文件源（如果是摄像头需要先初始化摄像头）。并在右上角选择这次是哪种检测（检测1：睡觉检测，检测2：违停检测）。如果是违停检测，需要先选定规范停车区域，下方有讲解。

可选步骤：在下方中间窗口选择检测相关的参数（后面有每个参数的详解）。

    在右下方选择是否保存结果与保存路径。

随后就可以在右下方点击开始按钮进行检测了。

### 其余补充：
（1）修改睡觉计时

可修改 target_timing 方法， duration 为持续睡觉目标的计时，可修改约 893 行的代码自定义触发警报时间，同时可修改约 900 行的代码来自定义消失时间就取消计时的时间。

（2）自定义规范停车区域

在中央的两个展示区域中利用鼠标进行操作，左键添加结点，右键删除结点，左键长按拖动结点，程序会根据所选结点进行自动绘制闭合区域并展示出来，两个区域均可操作。

## 
# 训练模型
本人训练的睡觉姿势检测模型有点过拟合，并且当时训练用的GPU也不是很好。如果你有自己的数据集，也可以训练出自己的模型。

## （1）准备数据集
所有数据集<font style="color:#DF2A3F;">必须</font>放在主目录下的 <font style="color:#DF2A3F;">dataset </font>目录下，可用bvn1、bvn2......进行分类，每个bvn都是这次训练的全部数据。具体目录结构如下：

```plain
main/
│
├── dataset/
│   ├── bvn/
│   │   ├── images/
│   │   │   ├── train/
│   │   │   └── val/
│   │   └── labels/
│   │       ├── train/
│   │       └── val/
```

images <font style="color:#DF2A3F;">只</font>放照片， labels <font style="color:#DF2A3F;">只</font>放与标签数据文件，且 images 下的 train 和 val 文件名<font style="color:#DF2A3F;">必须</font>与 labels 下的文件名<font style="color:#DF2A3F;">一一对应</font><font style="color:#000000;">。train 为训练集，val 为验证集，建议比例可以为 7:3</font>

## （2）准备yaml配置文件
可以直接编辑原有的 yolo_bvn.yaml 文件。

![](https://cdn.nlark.com/yuque/0/2024/png/50508020/1734589007732-4ef55e34-ea55-400d-897f-a94b5fc914d6.png)

path 为 dataset 下用于本次训练的全部数据的文件目录，为相对路径（/dataset 下），具体可参照 （1）准备数据集 中的文件目录结构。

train 为用于训练的照片路径，为相对路径（/dataset/path 下，示例为 /dataset/bvn 下）。只需要填写训练照片的路径即可。

train 为用于验证的照片路径，为相对路径（/dataset/path 下，示例为 /dataset/bvn 下）。只需要填写验证照片的路径即可。

test 为测试路径，可不填写，可自行测试。

![](https://cdn.nlark.com/yuque/0/2024/png/50508020/1734589326560-277e30ae-fa3a-430d-a867-f0e2b93a2bb3.png)

names 为标签类型的名字，你训练的是睡觉的可填sleeping，训练的是电动车可填vehicle。这决定了你使用该模型检测到目标后显示框的名字。如果训练数据是有多个类型、多个分类的，可继续添加，例如：  
![](https://cdn.nlark.com/yuque/0/2024/png/50508020/1734589487464-675eb875-e483-4a0d-afcc-f556f4627d84.png)

这与你的训练数据有关。

## （3）编写训练文件并开始训练
**1、编写训练文件**

可直接编写项目中的 yolov8_train.py

![](https://cdn.nlark.com/yuque/0/2024/png/50508020/1734589604391-29e998ee-7d6e-40d1-82fe-68b393c758ee.png)

第一行为导入包

第二到四行只可选一个，第一个为添加了SEA注意力机制的yaml文件，第二个为添加了CBAM注意力机制的文件，第三个为普通训练。

第5行注释的意思为，如果是在终端执行该文件，就需要将下面的workers改为1，如果是直接在pycharm中运行就为0。

第6行参数解释，data 为刚编写完的yaml文件，epochs 为训练的最大轮数，patience 为在最大轮数内，训练多少轮效果没有提升后就会自动停止训练。

**2、开始训练**

编写完即可在pycharm中右键运行该文件。训练完成后会自动保存最后一次训练的模型以及训练效果最好的一次模型，还有一些训练过程中一些参数的变化。

**3、验证**

运行 yolov8_val.py 即可



# 补充
## 参数说明
程序中的 

**conf **为置信度，为显示目标的最低得分，只有目标的得分超过该数值才会显示出来。太大可能导致目标遗漏，太小可能导致错误目标被检测出来。

**iou** 越小，同一目标的重复框就越多。

**linewidth** 为绘制框的线条粗细。

检测2中的**开启变色绘图**选项，为在区域内的目标为绿色框，在区域外的目标为红色框，为了可视化违停目标。

## 不足与可能改进
因为是毕业设计，写的很潦草，仍然有很多的不足和BUG，下面是可能改进的地方。

### （1）睡觉检测中的 id 转移
因为用的是 ByteTrack 进行追踪，获得每个目标的编号，针对编号进行计时，本来想要的效果是每个人都有一个自己的独特编号，但在目标消失和出现的时候就会出现编号转移的情况。具体举例说明：有三个同学在睡觉，分别是A、B、C，ByteTrack 会赋予他们每个人一个 id，例如 A:1, B:2 , C:3，此时如果A同学不睡觉了，那么B同学或者C同学的编号就会发生变化，可能是 B:1, C:2，或者 B:2, C:1，程序中是根据编号进行计时的，1编号始终没消失，所以计时就会一直进行，等到超过5秒就会报警，但此时触发报警的是B同学或者C同学，而不是原先的A同学。

