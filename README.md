# Real-Time Object Recognition
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)&nbsp;
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)&nbsp;
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)&nbsp;
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)&nbsp;
![Sckit Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)&nbsp;
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)&nbsp;

<br>

This project addresses the problem of object recognition by training and evaluating YOLO for efficiency and accuracy.
<br><br>
Performance Metrics:<br>

| Name  | Precision | Recall | F1 Score | mAP.5 | mAP.95 | FPS   |
| :---- | :-------- | :----- | :------- | :---- | :----- | :---- |
|YOLO |0.751 |0.695 |0.722 |0.757 |0.544 |~131|

<br>

YOLO: This folder contains the jupyter notebooks used for pre-processing, training and testing YOLO (You Only Look Once) model. The 5-fold folder contains the training output of each of the 5 folds during stratified 5-fold cross validation. The result folder contains the weights (best) of the model trained on the entire dataset. 
