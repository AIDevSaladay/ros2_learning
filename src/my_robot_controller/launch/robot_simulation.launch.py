from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_controller',
            executable='battery_node',
            name='battery_node',
            output='screen'),
        
        Node(
            package='my_robot_controller',
            executable='motor_simulator',
            name='motor_simulator',
            output='screen'),
        
        Node(
            package='my_robot_controller',
            executable='system_monitor',
            name='system_monitor',
            output='screen'),
        
        Node(
            package='my_robot_controller',
            executable='temperature_sensor',
            name='temperature_sensor',
            output='screen'),
        
        Node(
            package='my_robot_controller',
            executable='charging_station',
            name='charging_station',
            output='screen'),
        
        Node(
            package='my_robot_controller',
            executable='distance_sensor',
            name='distance_sensor',
            output='screen'),
    ])