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

class   DisabilityAssistant:

    def __init__(self, host="localhost", port="2000"):
        self.image_subscriber = ImageSubscriber()
        self.plugin_master = PluginMaster()
        self.host = host
        self.port = port
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out  = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        self.frames = []

    def ros_connect(self, args=None):
        rclpy.init(args=args)

    def get_frame(self):
        file = "assets/images/street.png"
        frame = cv2.imread(file)
        return frame

    def start(self):
        try:
            self.ros_connect()
            # while (True): # if connection is true
            frame = self.get_frame()
            self.frames.append(self.plugin_master.start(frame))
        except Exception as _exp:
            print("Error", _exp)
        
    def __del__(self):
        for frame in self.frames:
            self.out.write(frame)