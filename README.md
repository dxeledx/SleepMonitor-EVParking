安装Anaconda  

创建虚拟环境  conda create -n yolov8 python==3.12  #yolov8为虚拟环境的名称 制定python版本为3.12

激活虚拟环境  conda activate yolov8

配置清华源（修改默认）  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

安装pytorch  根据自己的cuda版本安装  conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia

在github上下载yolov8  进入该文件夹后用pip指令安装   pip install -e .

安装包  pip install PyQt5 opencv-python pygame
