import  cv2
import  rclpy
from    rclpy.node \
        import  Node
from    cv_bridge \
        import  CvBridge

class   ImageSubscriber(Node):

    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/car/camera1/image_raw',
            self.image_callback,
            10)
        self.bridge = CvBridge()
        self.latest_image = None

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            self.latest_image = cv_image
        except Exception as e:
            self.get_logger().info('Error: {}'.format(e))


# You can use the following function to process the images
def process_images(node):
    while rclpy.ok():
        if node.latest_image is not None:
            cv2.imshow('Image', node.latest_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    
    process_thread = threading.Thread(target=process_images, args=(image_subscriber,))
    process_thread.start()
    
    rclpy.spin(image_subscriber)

    image_subscriber.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

