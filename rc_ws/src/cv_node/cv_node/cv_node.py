import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from ultralytics import YOLO

class ZED2YOLOSubscriber(Node):
    def __init__(self):
        super().__init__('zed2_yolo_subscriber')

        # YOLO model setup
        self.yolo_model = YOLO('yolo-Weights/yolov8n.pt')

        # Bridge to convert ROS Image messages to OpenCV images
        self.bridge = CvBridge()

        # Subscribing to the ZED2 Camera image topic
        self.image_sub = self.create_subscription(
            Image,
            '/zed2/zed_node/left/image_rect_color',
            self.image_callback,
            10
        )

        self.get_logger().info('ZED2 Camera Node with YOLO Started')

    def image_callback(self, msg):
        self.get_logger().info('Received an image')
        
        # Convert the ROS Image message to an OpenCV image
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # Perform YOLO detection
        results = self.yolo_model(cv_image)

        # Get the first image result
        result_image = np.squeeze(results.render())  # YOLO result rendering (bounding boxes, labels)

        # Display the image with YOLO detections
        cv2.imshow("YOLOv8 Detections", result_image)
        cv2.waitKey(1)  # Required to display the image

def main(args=None):
    rclpy.init(args=args)

    zed2_yolo_subscriber = ZED2YOLOSubscriber()

    try:
        rclpy.spin(zed2_yolo_subscriber)
    except KeyboardInterrupt:
        pass

    zed2_yolo_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
