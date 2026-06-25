#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg  import Float32, Bool


class MotorSimulator(Node):
    def __init__(self):
        super().__init__('motor_simulator')
        
        self.current_speed = 0.0
        self.current_angular = 0.0
        self.battery_level = 0.0
        self.is_moving = False
        
        self.cmd_subscriber = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.distance_subscriber = self.create_subscription(Float32, '/distance', self.distance_callback, 10)
        self.battery_subscriber = self.create_subscription(Float32, '/battery_level', self.battery_callback, 10)
        self.state_publisher = self.create_publisher(Bool, '/motor_state', 10)
        
        self.timer = self.create_timer(0.5, self.publish_state)
        self.get_logger().info('Motor Simulator started')
    
    def distance_callback(self, msg):
        if msg.data < 0.5:
            self.is_moving = False
            self.get_logger().error('ERROR! Motor stopping')
        
    def battery_callback(self, msg: Float32):
        self.battery_level = msg.data
        
    def cmd_vel_callback(self, msg: Twist):
        if self.battery_level < 5.0:
            self.get_logger().error('Battery too low! cannot move.')
            self.current_speed = 0.0
            self.current_angular = 0.0
            self.is_moving = False
            return
        
        self.current_speed = msg.linear.x
        self.current_angular = msg.angular.z
        self.is_moving = abs(self.current_speed) > 0.01 or abs(self.current_angular) > 0.01
        
        if self.is_moving:
            self.get_logger().info(f'Motors running: speed={self.current_speed:.2f} m/s,'
                                   f'angular={self.current_angular:.2f} rad/s')
        else:
            self.get_logger().info('Motors stopped')
    
    def publish_state(self):
        msg = Bool()
        msg.data = self.is_moving
        self.state_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MotorSimulator()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()