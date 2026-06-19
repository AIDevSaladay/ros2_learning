#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from time import strftime, localtime

class MyFirstNode(Node):
    def __init__(self):
        super().__init__('my_first_node')
        self.get_logger().info('Привет из ROS 2!')
        self.create_timer(0.5, self.slow_timer_callback)
        self.create_timer(0.2, self.fast_timer_callback)

    def fast_timer_callback(self):
        self.get_logger().info('Fast timer')
        
    def slow_timer_callback(self):
        self.get_logger().info('Slow timer')
                               
                               
def main(args=None):
    rclpy.init(args=args)
    node = MyFirstNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == '__main__':
    main()
