#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32


class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        
        self.temp = 25.0
        self.is_moving = False
        self.temp_pub = self.create_publisher(Float32, '/temperature', 10)
        self.motor_sub = self.create_subscription(Bool, '/motor_state', self.motor_callback, 10)
        self.timer = self.create_timer(2.0, self.change_temp)
        self.get_logger().info('Temperature Sensor start')
        
        
    def motor_callback(self, msg: Bool):
        self.is_moving = msg.data
    
    def change_temp(self):
        if self.is_moving:
            self.temp += 2.0
        else:
            self.temp -= 1.0
        if self.temp < 25.0:
            self.temp = 25.0
        if self.temp > 80.0:
            self.temp = 80.0
        msg = Float32()
        msg.data = self.temp
        self.temp_pub.publish(msg)
        if self.temp <= 70.0:
            self.get_logger().info(f'INFO - temperature {self.temp}')
        else:
            self.get_logger().warn(f'WARNING - temperature {self.temp}')


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()