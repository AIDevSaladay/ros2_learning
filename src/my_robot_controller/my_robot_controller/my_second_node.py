#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MySecondNode(Node):
    def __init__(self):
        super().__init__('my_second_node')
        self.create_timer(2, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Node 2 is alive!')
                               
                               
def main(args=None):
    rclpy.init(args=args)
    node = MySecondNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == '__main__':
    main()
