#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotNewsStation(Node):
    def __init__(self):
        super().__init__('robot_news_station')

        # Создаём Publisher
        self.publisher_ = self.create_publisher(String, 'robot_news', 10)
        self.timer = self.create_timer(0.5, self.publish_news)
        self.counter = 0
        self.get_logger().info('Robot News Station запущена!')

    def publish_news(self):
        msg = String()
        msg.data = f'Новость #{self.counter}: Робот работает'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикую: "{msg.data}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
