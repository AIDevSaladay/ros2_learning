from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='saladay@yandex.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_first_node = my_robot_controller.my_first_node:main',
            'my_second_node = my_robot_controller.my_second_node:main',
            'robot_news_station = my_robot_controller.robot_news_station:main',
            'smartphone = my_robot_controller.smartphone:main',
            'traffic_light = my_robot_controller.traffic_light:main',
            'car = my_robot_controller.car:main',
            'battery_simulator = my_robot_controller.battery_simulator:main',
            'battery_monitor = my_robot_controller.battery_monitor:main',
            'number_publisher = my_robot_controller.number_publisher:main',
            'number_counter = my_robot_controller.number_counter:main',
            'battery_node = my_robot_controller.battery_node:main',
            'motor_simulator = my_robot_controller.motor_simulator:main',
            'system_monitor = my_robot_controller.system_monitor:main',
            'temperature_sensor = my_robot_controller.temperature_sensor:main',
            'charging_station = my_robot_controller.charging_station:main',
            
        ],
    },
)
