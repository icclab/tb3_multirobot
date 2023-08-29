# tb3_multirobot

This project starts from the nav2 bringup examples in ROS2. Differently, form the proposed multirobot example where each tb3 has his own RviZ and map, here the two
tb3 are spawned on the same single shared map and one RviZ instance is used for visualization.

Launch command is:

    ros2 launch tb3_multirobot two_tb3_simulation_launch.py headless:=False use_composition:=False 

In RviZ the initial position can be adjusted if needed, using the tool configurator and setting the initial pose topic using either robot_1 or robot_2 prefix. 
The Goal Pose in RviZ can also be similarly configured using the tool configurator.

Under the scripts folder there is a basic python3 script (BasicNavigator.py) to move the robot. Change the namespace for the robot to move either robot_1 or robot_2.
