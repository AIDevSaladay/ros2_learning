#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class BatterySimulator(Node):
    def __init__(self):
        super().__init__('battery_simulator')

        # Создаём Publisher
        self.publisher_ = self.create_publisher(Float32, 'battery_level', 10)
        self.timer = self.create_timer(1, self.uncharge)
        self.get_logger().info('Узел батареи запущен')
        self.battery = 100.00

    def uncharge(self):
        msg = Float32()
        msg.data = self.battery
        self.publisher_.publish(msg)
        self.get_logger().info(f'Уровень батареи: "{msg.data}"')
        self.battery = max(self.battery - 1, 0.0)


def main(args=None):
    rclpy.init(args=args)
    node = BatterySimulator()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
