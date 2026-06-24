# Узлы
- battery_node - состояние батареи
- motor_simulator - имитация движения моторами
- system_monitor - системный монитор, вся информаци о системе
- temperature_sensor - датчик температуры


# Топики
- /battery_level - состояние батареи, Float32
- /motor_state - состояние моторов, Bool
- /system_status - статус всей системы, String
- /temperature - температура системы, Float32

# Инструкция
cd ~
colcon build --packages-select my_robot_controller --symlink-install
ros2 launch my_robot_controller robot_simulation.launch.py 

В отдельной консоли публикуем движение робота:
Вперед:
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
Стоп:
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
Поворот:
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}"

# Схема связей
battery_node -> battery_level -> motor_simulator
                              -> system_monitor

cmd_vel -> motor_simulator -> motor_state -> battery_node
                                          -> system_monitor
                                          -> temperature_sensor

system_monitor -> system_status

temperature_sensor -> temperature -> system_monitor