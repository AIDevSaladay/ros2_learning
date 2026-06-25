#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from random import uniform


class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        self.distance_pub = self.create_publisher(Float32, '/distance', 10)
        self.timer = self.create_timer(1.0, self.check_distance)
        self.get_logger().info('Distance started')
        
    def check_distance(self):
        msg = Float32()
        msg.data = uniform(0.5, 5.0)
        self.distance_pub.publish(msg)
        if msg.data  < 1.0:
            self.get_logger().warn(f'WARNING! Obstacle close! (distance: {msg.data} m)')
        else:
            self.get_logger().info(f'Distance {msg.data} m')


def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()