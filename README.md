# Узлы
- my_first_node - два таймера - быстрый и медленный
- my_second_node - тестовый узел
- robot_news_station - публикует случайное число от 1 до 100 в топик robot_news каждые 0.5 сек
- smartphone - получает новости из топика robot_news (после изменений уже не получает)
- traffic_light - светофор - публикует в топик traffic_light каждые 3 секунды новый свет 
- car - получает свет из traffic_light и выводит соответствующее свету действие

# Топики
- /robot_news
- /traffic_light

# Инструкция
cd ~
colcon build --packages-select my_robot_controller --symlink-install

В разных консолях запустить ноды:
source install/setup.bash 
ros2 run my_robot_controller "node_name"
Вместо node_name использовать имена узлов из списка