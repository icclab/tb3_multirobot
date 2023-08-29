# tb3_multirobot localicazation and navigation

This project starts from the nav2 bringup examples in ROS2. Differently, form the proposed multirobot example where each tb3 has his own RviZ and map, here the two
tb3 are spawned on the same single shared map and one RviZ instance is used for visualization.

Launch command is:

    ros2 launch tb3_multirobot two_tb3_simulation_launch.py headless:=False use_composition:=False 

In RviZ the initial position can be adjusted if needed, using the tool configurator and setting the initial pose topic using either robot_1 or robot_2 prefix. 
The 2D Goal Pose in RviZ can also be similarly configured using the tool configurator.

Under the scripts folder there is a basic python3 script (BasicNavigator.py) to move the robot. Change the namespace for the robot to move either robot_1 or robot_2.


# tb3_multirobot SLAM

To launch the project with SLAM functionalities we need the following project to merge the two maps into one single map https://github.com/icclab/mapMergeForMultiRobotMapping-ROS2
Clone and build also this repo into your workspace. The configuration of the map topics is pretty simple in the merge_map.py file.

After building and sourcing your workspace use the following command to launch the SLAM project:

        ros2 launch tb3_multirobot two_tb3_simulation_launch.py headless:=False use_composition:=False slam:=True

Again you can use RviZ and the 2D Goal Pose in RviZ configured for either of the robots, or the BasicNavigator.py script.

You can save the obtained map for instance with the following command.

    ros2 run nav2_map_server map_saver_cli -f my_map

