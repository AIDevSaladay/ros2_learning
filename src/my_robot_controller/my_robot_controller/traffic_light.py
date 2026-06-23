#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32
import random


class TrafficLightStation(Node):
    def __init__(self):
        super().__init__('traffic_light_station')

        # Создаём Publisher
        self.publisher_ = self.create_publisher(String, 'traffic_light', 10)
        self.timer = self.create_timer(3, self.publish_color)
        self.get_logger().info('Светофор запущен!')
        self.color = 0

    def publish_color(self):
        COLORS = ["RED", "YELLOW", "GREEN"]
        self.color %= 3
        msg = String()
        msg.data = COLORS[self.color]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикую: "{msg.data}"')
        self.color += 1


def main(args=None):
    rclpy.init(args=args)
    node = TrafficLightStation()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
