#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class Car(Node):
    def __init__(self):
        super().__init__('car')

        # Создаём Publisher
        self.subscriber_ = self.create_subscription(String, 'traffic_light', self.callback_color, 10)
        self.get_logger().info('Car готов принимать цвета сфетофора')

    def callback_color(self, msg):
        reactions = {"RED": "Остановка!", "YELLOW": "Замедляюсь...", "GREEN": "Еду!"}
        self.get_logger().info(f'{reactions.get(msg.data, "ОШИБКА!")}')


def main(args=None):
    rclpy.init(args=args)
    node = Car()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
