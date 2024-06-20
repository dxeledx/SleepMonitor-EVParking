from ultralytics import YOLO
model = YOLO("./models/sleeping.pt")
model.val(data = "./yolo_bvn.yaml", workers = 0, imgsz=640, batch=16, conf=0.25, iou=0.6, plots = True)

#, device = 'cpu'
# #workers 终端1  .py0