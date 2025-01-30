from pathlib import WindowsPath
from ultralytics import YOLO
import os

ksplit = 0

ds_yamls = [
    WindowsPath('C:/D_Drive/Homework/ALDA/YOLO/Dataset/YOLO/5-Fold_Cross-val/split_1/split_1_dataset.yaml'),
    WindowsPath('C:/D_Drive/Homework/ALDA/YOLO/Dataset/YOLO/5-Fold_Cross-val/split_2/split_2_dataset.yaml'),
    WindowsPath('C:/D_Drive/Homework/ALDA/YOLO/Dataset/YOLO/5-Fold_Cross-val/split_3/split_3_dataset.yaml'),
    WindowsPath('C:/D_Drive/Homework/ALDA/YOLO/Dataset/YOLO/5-Fold_Cross-val/split_4/split_4_dataset.yaml'),
    WindowsPath('C:/D_Drive/Homework/ALDA/YOLO/Dataset/YOLO/5-Fold_Cross-val/split_5/split_5_dataset.yaml')
    ]

if __name__ == '__main__':
    os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

    # Define your additional arguments here
    project = "all_demo"
    epochs = 15
    imgsz = 512

    for k in range(ksplit):
        dataset_yaml = ds_yamls[ksplit]
        model = YOLO("yolov8m.pt", task="detect")  # load a pretrained model
        model.train(data=dataset_yaml, epochs=epochs, project=project, imgsz=imgsz)  # include any train arguments
        results = model.metrics  # save output metrics for further analysis

    print(results)