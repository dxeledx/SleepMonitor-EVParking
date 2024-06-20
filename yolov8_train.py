from ultralytics import YOLO
model = YOLO('./ultralytics/cfg/models/v8/SEAtt_yolov8.yaml').load("./yolov8n.pt")
#model = YOLO('./ultralytics/cfg/models/v8/CBAM_yolov8.yaml').load("./yolov8n.pt")
#model = YOLO("./yolov8n.pt")
#workers 终端1  .py0
model.train(data = "./yolo_bvn.yaml", workers = 0, epochs = 50, batch = -1, patience = 50)#, device = 'cpu'