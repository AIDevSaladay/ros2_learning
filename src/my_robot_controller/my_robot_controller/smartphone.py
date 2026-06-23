#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class Smartphone(Node):
    def __init__(self):
        super().__init__('smartphone')

        # Создаём Publisher
        self.subscriber_ = self.create_subscription(String, 'robot_news', self.callback_news, 10)
        self.get_logger().info('Smartphone готов принимать новости')

    def callback_news(self, msg):
        self.get_logger().info(f'📱 Получена новость: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = Smartphone()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
