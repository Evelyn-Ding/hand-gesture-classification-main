# Hand-gesture-recognition
**A Computer Vision based pipeline combining hand-object detection and hand gesture classification for home automation.**


*Please check out our slides: https://docs.google.com/presentation/d/1rNwsgJgCdeZPomP2Br9HXsqSbKwOMSd-fWF6HW_xRMg/edit?usp=sharing

Problem: Patients with neuromuscular diseases have a hard time controlling the settings of their home, including lights, thermostat, and volume levels.

Motivation: What if a simple hand gesture could accomplish this day-to-day task?

Method: We created a datset with over 700 images taken by a webcam. Then we utilized Roboflow to annotate & label the data using 3 classes—fist, hand, and peace sign—by drawing a bounding box around each gesture and labeling its class. Then we implemented the Yolo-v5 model. It is unique in that it reframes object detection as a single regression problem. It's extremely fast and efficient (45FPS, <25 milliseconds of latency), reasons globally and sees the entire image, and has generalizable representation of objects.

 
