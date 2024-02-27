import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

import pygame


class TeleopPublisher(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.publisher_ = self.create_publisher(Twist, '/car/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.callback)  # [s]

        self.control_msg = Twist()

        self.control_msg.linear.x = 0.0
        self.control_msg.linear.y = 0.0
        self.control_msg.linear.z = 0.0
        self.control_msg.angular.x = 0.0
        self.control_msg.angular.y = 0.0
        self.control_msg.angular.z = 0.0

        self.publisher_.publish(self.control_msg)

        self.w = False
        self.a = False
        self.s = False
        self.d = False

        self.pre_steering = None
        self.pre_throttle = None


    def callback(self):
        if self.a and self.d:
            self.control_msg.angular.z = 0.0
        elif self.a:
            self.control_msg.angular.z = 1.0
        elif self.d:
            self.control_msg.angular.z = -1.0
        else:
            self.control_msg.angular.z = 0.0

        if self.w and self.s:
            self.control_msg.linear.x = 0.0
        elif self.w:
            self.control_msg.linear.x = 1.0
        elif self.s:
            self.control_msg.linear.x = -1.0
        else:
            self.control_msg.linear.x = 0.0

        self.control_msg.linear.x *= 3

        if (self.pre_steering is None or self.pre_steering != self.control_msg.angular.z) or \
            (self.pre_throttle is None or self.pre_throttle != self.control_msg.linear.x):
            self.pre_steering = self.control_msg.angular.z
            self.pre_throttle = self.control_msg.linear.x
            self.publisher_.publish(self.control_msg)
            # self.get_logger().info('')


def main(args=None):
    pygame.init()

    pygame.display.set_mode((300, 200))
    pygame.display.set_caption("Controller (w, a, s, d)")

    rclpy.init(args=args)

    teleop_publisher = TeleopPublisher()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        teleop_publisher.w = keys[pygame.K_w]
        teleop_publisher.a = keys[pygame.K_a]
        teleop_publisher.s = keys[pygame.K_s]
        teleop_publisher.d = keys[pygame.K_d]

        rclpy.spin_once(teleop_publisher)

    teleop_publisher.destroy_node()
    rclpy.shutdown()

    pygame.quit()


if __name__ == '__main__':
    main()
