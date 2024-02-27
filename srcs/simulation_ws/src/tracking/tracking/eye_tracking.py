import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Point

import cv2
from gaze_tracking import GazeTracking


class EyePub(Node):
    def __init__(self):
        super().__init__('eye_pub_node')
        self.publisher_ = self.create_publisher(Point, 'eye', 10)
        self.timer_ = self.create_timer(0.1, self.callback)  # [s]

        self.eye = Point()
        self.eye.x = 0.0
        self.eye.y = 0.0
        self.eye.z = 0.0

        self.publisher_.publish(self.eye)

        self.gaze = GazeTracking()
        self.webcam = cv2.VideoCapture(0)


    def callback(self):
        _, frame = self.webcam.read()
        self.gaze.refresh(frame)
        frame = self.gaze.annotated_frame()

        if self.gaze.pupil_left_coords() is not None and self.gaze.pupil_right_coords() is not None:
            left_x, left_y = self.gaze.pupil_left_coords()
            right_x, right_y = self.gaze.pupil_right_coords()

            center_x = min((left_x + right_x) / 2, 600)
            center_y = min((left_y + right_y) / 2, 400) + 100

            distance = ((left_x - right_x) ** 2 + (left_y - right_y) ** 2) ** 0.5
            distance = max(distance, 60)
            distance = min(distance, 120)

            self.eye.x = (center_x * 0.4 / 600 - 0.2) * -1
            self.eye.y = (distance - 60) * 0.4 / 60 - 0.2
            self.eye.z = (center_y * 0.4 / 600 - 0.2) * -1

            self.publisher_.publish(self.eye)
            # self.get_logger().info('')

        frame = cv2.flip(frame, 1) 
        cv2.imshow("Eye Tracking", frame)
        cv2.waitKey(100)
    
    
    def __del__(self):
        self.webcam.release()
        cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args)

    eye_pub = EyePub()

    rclpy.spin(eye_pub)

    eye_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
