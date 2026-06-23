#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32
import random


class RobotNewsStation(Node):
    def __init__(self):
        super().__init__('robot_news_station')

        # Создаём Publisher
        self.publisher_ = self.create_publisher(Int32, 'robot_news', 10)
        self.timer = self.create_timer(0.5, self.publish_news)
        self.get_logger().info('Robot News Station запущена!')

    def publish_news(self):
        msg = Int32()
        random_number = random.randint(1, 100)
        msg.data = random_number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикую: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
