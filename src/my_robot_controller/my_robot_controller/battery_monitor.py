#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32



class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')

        # Создаём Publisher
        self.subscriber_ = self.create_subscription(Float32, 'battery_level', self.callback_info, 10)
        self.get_logger().info('Мониторинг уровня заряда батерии запущен')

    def callback_info(self, msg):
        if msg.data < 20:
            self.get_logger().info(f"КРИТИЧЕСКИЙ УРОВЕНЬ!")
        elif msg.data > 50:
            self.get_logger().info(f"Батарея OK")
        else:
            self.get_logger().info(f"Батарея разряжается")


def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
