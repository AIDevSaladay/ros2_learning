#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String


class SystemMonitor(Node):
    def __init__(self):
        super().__init__('system_monitor')
        
        self.battery_level = 100.0
        self.is_moving = False
        self.temp = 25.0
        
        self.battery_sub = self.create_subscription(Float32, '/battery_level', self.battery_callback, 10)
        self.motor_sub = self.create_subscription(Bool, '/motor_state', self.motor_callback, 10)
        self.temp_sub = self.create_subscription(Float32, '/temperature', self.temp_callback, 10)
        self.status_pub = self.create_publisher(String, '/system_status', 10)
        self.timer = self.create_timer(3.0, self.publish_status)
        self.get_logger().info('System Monitor started')
        
    def battery_callback(self, msg: Float32):
        self.battery_level = msg.data
    
    def motor_callback(self, msg: Bool):
        self.is_moving = msg.data
        
    def temp_callback(self, msg: Float32):
        self.temp = msg.data
    
    def publish_status(self):
        if self.battery_level < 5.0:
            status = 'CRITICAL - System shutdown imminent'
        elif self.battery_level < 20:
            status = f'WARNING - Low battery ({self.battery_level:.1f}) Temperature: {self.temp:.1f}'
        elif self.is_moving:
            status = f'ACTIVE - Robot moving (Battery: {self.battery_level:.1f}, Temperature: {self.temp:.1f})'
        else:
            status = f'IDLE - Ready (Battery: {self.battery_level:.1f}) Temperature: {self.temp:.1f}'
        if self.temp > 75.0:
            status += '. CRITICAL TEMPERATURE'
        elif self.temp > 70.0:
            status += '. OVERHEATING WARNING'
        
        msg = String()
        msg.data = status
        self.status_pub.publish(msg)
        self.get_logger().info(f'System Status: {status}')
        

def main(args=None):
    rclpy.init(args=args)
    node = SystemMonitor()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()