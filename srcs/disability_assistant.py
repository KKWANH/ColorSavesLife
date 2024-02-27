import  threading
import  cv2
import  rclpy

from    sensor_msgs.msg \
        import  Image
from    image_subscriber \
        import  ImageSubscriber
from    plugins.plugin_master \
        import  PluginMaster
from    plugins.plugin \
        import  Plugin
from image_subscriber import ImageSubscriber
import rclpy
import threading

class   DisabilityAssistant:

    def __init__(self, host="localhost", port="2000"):
        self.plugin_master = PluginMaster()
        rclpy.init(args=None)
        self.host = host
        self.port = port
        self.image_subscriber_ = ImageSubscriber()

    def process_image(self):
        try:
            while rclpy.ok():
                if self.image_subscriber_.latest_image is not None:
                    frame = self.image_subscriber_.latest_image
                    frame = self.plugin_master.start(frame)
                    cv2.imshow("Frame", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        except Exception as _exp:
            print("Error", _exp)

    def start(self):
        process_thread = threading.Thread(target=self.process_image, args=())
        process_thread.start()
        rclpy.spin(self.image_subscriber_)
        self.image_subscriber_.destroy_node()
        rclpy.shutdown()
