#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int64
import random


class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')

        # Создаём Publisher
        self.publisher_ = self.create_publisher(Int64, 'number', 10)
        self.timer = self.create_timer(1, self.publish_number)
        self.get_logger().info('Counter System запущен!')
        self.number = 0

    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикую: "{msg.data}"')
        self.number += 1


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
