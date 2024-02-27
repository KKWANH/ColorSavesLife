import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ament_index_python.packages import get_package_share_directory

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('test_publisher')
        self.publisher_ = self.create_publisher(Image, 'car/camera1/image_raw', 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        self.bridge = CvBridge()
        
        package_share_directory = get_package_share_directory('test_publisher')
        image_path = package_share_directory + '/resource/test.jpg'

        self.image = cv2.imread(image_path)
        
    def timer_callback(self):
        msg = self.bridge.cv2_to_imgmsg(self.image, encoding="bgr8")
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing image')

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


