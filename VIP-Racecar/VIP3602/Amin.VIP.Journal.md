### Week 3:
#### Post Meeting Notes:
Assigned object detection project, will begin researching which model and approach to use.

#### Work:
* Read and noted the VIP Project + F1/10th + ICRA Competition guidelines.
	* Determined the high level objectives of the project.
* Read through some of the F1/10th slides to gauge some of the technical objectives. Pulled this high level overview:
![[overview.png]]

#### Results:
* Decided on using YOLO Model for object detection, likely going to use v5n to remain computationally efficient and lightweight.
\pagebreak
### Week 4:
#### Post Meeting Notes:
No notes

#### Work:
* Installing PyTorch to get YOLO set up 
* Wrote python scripts to utilize YOLO

#### Results:
* PyTorch/Ultralytics and YOLO Model are set up, tested with a generic stop sign image to get some benchmark statistics, shown below.
* Live feed using webcam is working, next step will be to integrate the ZedCamera.
* With live bounding boxes made, the next step will be to implement a depth map and analyze for depth to object data.
* v8n seems to have some issues with detecting the right things but actual testing with the car will have to be done to see if it is really detrimental.
![[image.jpg]]
![[sample.avi]]
![[model_speed.png]]

### Week 5

#### Post Meeting Notes:
* Meeting cancelled due to weather

#### Work:
* Researched various depth calculation methods
	* Option 1: Bounding box 

#### Results:
* No results

### Week 6
#### Post Meeting Notes:

#### Work:
* Began developing ROS workspace for camera and object detection
* Compiled documentation and sample pieces of code to understand how to develop our system.
	* Checked out the sample code to subscribe to the camera image topics
	* Looked at a C++ implementation of YOLO as I want to optimize the code through the language and I was using Python before. 

#### Results:
