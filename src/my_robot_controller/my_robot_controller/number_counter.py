#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64



class NumberCounter(Node):
    def __init__(self):
        super().__init__('number_counter')

        # Создаём Publisher
        self.subscriber_ = self.create_subscription(Int64, 'number', self.callback_number, 10)
        self.get_logger().info('Number Counter запущен')
        self.count = 0
        self.summa = 0

    def callback_number(self, msg):
        self.summa += msg.data
        self.count += 1
        self.get_logger().info(f'{self.summa}')
        if self.count % 5 == 0:
            self.get_logger().info(f'Сумма после {self.count} чисел: {self.summa}')


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
