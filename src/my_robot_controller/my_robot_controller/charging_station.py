#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool


class ChargingStation(Node):
    def __init__(self):
        super().__init__('charging_station')
        
        self.battery_level = 100.0
        self.working = False
        self.battery_subscriber = self.create_subscription(Float32, '/battery_level', self.battery_callback, 10)
        self.charging_publisher = self.create_publisher(Bool, '/charging_command', 10)
        self.get_logger().info('Charging Station started')
        
    def battery_callback(self, msg: Float32):
        self.battery_level = msg.data
        if self.battery_level < 30:
            send_msg = Bool()
            send_msg.data = True
            self.charging_publisher.publish(send_msg)
            self.working = True
        elif self.battery_level >= 95:
            send_msg = Bool()
            send_msg.data = False
            self.charging_publisher.publish(send_msg)
            self.working = False
        if self.working:
            self.get_logger().info(f'✅ Battery chargin (Battery: {self.battery_level})')
        else:
            self.get_logger().info(f'❌Battery not chargin (Battery: {self.battery_level})')
        

def main(args=None):
    rclpy.init(args=args)
    node = ChargingStation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()