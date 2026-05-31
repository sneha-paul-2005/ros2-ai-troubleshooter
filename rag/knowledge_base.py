# ROSA Knowledge Base — 200+ ROS2 Jazzy Specific Entries

ROS2_KNOWLEDGE = [
    # --- GENERAL ROS2 ---
    {
        "topic": "Node not found",
        "content": "If a ROS2 node is not found, make sure the package is built with colcon build and the workspace is sourced with source install/setup.bash. Also check if the node is running with ros2 node list."
    },
    {
        "topic": "ROS2 environment not set up",
        "content": "If ROS2 commands are not found, source the ROS2 setup file with source /opt/ros/jazzy/setup.bash. Add it to ~/.bashrc to make it permanent. For ROS2 Jazzy specifically use the jazzy path."
    },
    {
        "topic": "Colcon build failed",
        "content": "If colcon build fails, check for missing dependencies with rosdep install --from-paths src --ignore-src -r -y. Make sure you are in the workspace root directory. Check for Python syntax errors in your code."
    },
    {
        "topic": "Package not found",
        "content": "If a ROS2 package is not found, install it with sudo apt install ros-jazzy-package-name. Source the workspace after installation. Use ros2 pkg list to see all available packages."
    },
    {
        "topic": "Topic not publishing",
        "content": "If a topic is not publishing, use ros2 topic list to check if it exists. Use ros2 topic hz /topic_name to check publish rate. Use ros2 topic echo /topic_name to see messages. Check the node publishing it is running."
    },
    {
        "topic": "ROS2 node crashes immediately",
        "content": "If a ROS2 node crashes immediately, check the error logs with ros2 run package node --ros-args --log-level DEBUG. Look for missing parameters or incorrect topic names. Check if required dependencies are running."
    },
    {
        "topic": "ROS2 service not available",
        "content": "If a ROS2 service is not available, check running services with ros2 service list. Make sure the node providing the service is running. Try calling it with ros2 service call /service_name service_type."
    },
    {
        "topic": "ROS2 parameter not set",
        "content": "If a ROS2 parameter is not set, use ros2 param list to see all parameters. Set a parameter with ros2 param set /node_name param_name value. Check the node default parameters in its source code."
    },
    {
        "topic": "ROS2 bag recording issues",
        "content": "If ros2 bag record is not working, make sure the topics exist with ros2 topic list. Record specific topics with ros2 bag record -o bag_name /topic1 /topic2. Check available disk space before recording."
    },
    {
        "topic": "ROS2 launch file not found",
        "content": "If a launch file is not found, make sure the package is built and sourced. Check the launch file path with ros2 pkg prefix package_name. Rebuild with colcon build --packages-select package_name."
    },
    {
        "topic": "ROS2 Jazzy installation",
        "content": "To install ROS2 Jazzy on Ubuntu 24.04, add the ROS2 apt repository, install ros-jazzy-desktop, and source /opt/ros/jazzy/setup.bash. Add source to ~/.bashrc for permanent setup."
    },
    {
        "topic": "ROS2 Jazzy Python packages",
        "content": "In ROS2 Jazzy, Python packages should be installed inside a virtual environment to avoid conflicts with system packages. Use python3 -m venv venv and source venv/bin/activate before pip install."
    },
    {
        "topic": "ROS2 Jazzy domain ID",
        "content": "ROS2 Jazzy uses DDS for communication. Set ROS_DOMAIN_ID to isolate your robot from others on the same network. Export ROS_DOMAIN_ID=0 in ~/.bashrc. All nodes must have the same domain ID to communicate."
    },
    {
        "topic": "ROS2 Jazzy QoS settings",
        "content": "ROS2 Jazzy uses Quality of Service profiles for topics. If topics are not communicating, check QoS compatibility. Use RELIABLE for critical data and BEST_EFFORT for sensor data. Mismatched QoS causes silent failures."
    },
    {
        "topic": "ROS2 Jazzy executor",
        "content": "ROS2 Jazzy supports SingleThreadedExecutor and MultiThreadedExecutor. Use MultiThreadedExecutor for nodes with multiple callbacks. Import with from rclpy.executors import MultiThreadedExecutor."
    },
    {
        "topic": "ROS2 workspace setup",
        "content": "To set up a ROS2 workspace, create a directory with mkdir -p ~/ros2_ws/src, run colcon build from the workspace root, and source install/setup.bash. Always source both /opt/ros/jazzy/setup.bash and install/setup.bash."
    },
    {
        "topic": "ROS2 node lifecycle",
        "content": "ROS2 Jazzy supports managed lifecycle nodes with states: unconfigured, inactive, active, finalized. Use lifecycle nodes for better control over node startup and shutdown. Import LifecycleNode from rclpy.lifecycle."
    },
    {
        "topic": "ROS2 composition",
        "content": "ROS2 Jazzy supports composable nodes that run in the same process to reduce overhead. Use ComponentManager and load nodes as components. This reduces latency and memory usage for multiple nodes."
    },
    {
        "topic": "ROS2 actions not working",
        "content": "If ROS2 actions are not working, check that the action server is running with ros2 action list. Send a goal with ros2 action send_goal /action_name action_type goal. Check for timeout issues in action client."
    },
    {
        "topic": "ROS2 topic bandwidth",
        "content": "If ROS2 topic bandwidth is too high, use ros2 topic bw /topic_name to measure it. Reduce image resolution or publish rate to lower bandwidth. Use compressed image topics for camera data."
    },

    # --- TURTLEBOT3 ---
    {
        "topic": "TurtleBot3 not moving",
        "content": "If TurtleBot3 is not moving, check that TURTLEBOT3_MODEL is set with export TURTLEBOT3_MODEL=burger. Make sure teleop node is running with ros2 run turtlebot3_teleop teleop_keyboard. Check /cmd_vel topic has a publisher."
    },
    {
        "topic": "TurtleBot3 model not set",
        "content": "TurtleBot3 requires the model environment variable to be set. Run export TURTLEBOT3_MODEL=burger for Burger model or export TURTLEBOT3_MODEL=waffle for Waffle model. Add it to ~/.bashrc to make it permanent."
    },
    {
        "topic": "TurtleBot3 package not found",
        "content": "If TurtleBot3 packages are not found, install them with sudo apt install ros-jazzy-turtlebot3 ros-jazzy-turtlebot3-gazebo ros-jazzy-turtlebot3-navigation2. Source ROS2 after installation."
    },
    {
        "topic": "TurtleBot3 teleop not working",
        "content": "If TurtleBot3 teleop is not working, run ros2 run turtlebot3_teleop teleop_keyboard. Make sure the terminal window with teleop is focused when pressing keys. Check that /cmd_vel topic is being published."
    },
    {
        "topic": "TurtleBot3 URDF not loading",
        "content": "If TurtleBot3 URDF is not loading, check that robot_state_publisher is running. Verify TURTLEBOT3_MODEL is set correctly. Make sure turtlebot3_description package is installed."
    },
    {
        "topic": "TurtleBot3 Jazzy compatibility",
        "content": "TurtleBot3 on ROS2 Jazzy requires ros-jazzy-turtlebot3 packages. Some older TurtleBot3 launch files may need updating for Jazzy. Use ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py for simulation."
    },
    {
        "topic": "TurtleBot3 SLAM mapping",
        "content": "To run SLAM with TurtleBot3, install ros-jazzy-slam-toolbox. Launch with ros2 launch turtlebot3_cartographer cartographer.launch.py. Save map with ros2 run nav2_map_server map_saver_cli -f map_name."
    },
    {
        "topic": "TurtleBot3 waffle vs burger",
        "content": "TurtleBot3 Burger is smaller with 360 degree LiDAR. TurtleBot3 Waffle has a camera and more powerful hardware. Set TURTLEBOT3_MODEL=burger or TURTLEBOT3_MODEL=waffle based on your robot. They have different URDF files."
    },

    # --- GAZEBO ---
    {
        "topic": "Gazebo not launching",
        "content": "If Gazebo fails to launch, source ROS2 setup with source /opt/ros/jazzy/setup.bash. Check that turtlebot3_gazebo package is installed. Try killing old Gazebo processes with pkill -f gazebo."
    },
    {
        "topic": "Gazebo world not loading",
        "content": "If Gazebo world is not loading, check that the world file exists. Set the correct world path in the launch file. Try launching with a simple empty world first to isolate the issue."
    },
    {
        "topic": "Gazebo robot not spawning",
        "content": "If the robot is not spawning in Gazebo, check that the URDF is valid. Make sure the spawn_entity node is running. Check Gazebo logs for spawn errors. Try respawning with ros2 run gazebo_ros spawn_entity.py."
    },
    {
        "topic": "Gazebo and ROS2 not communicating",
        "content": "If Gazebo and ROS2 are not communicating, check that ros_gz_bridge is running. Verify the bridge topics are correctly mapped. Make sure ros-jazzy-ros-gz-bridge package is installed."
    },
    {
        "topic": "Gazebo simulation running slow",
        "content": "If Gazebo simulation is running slowly, reduce the simulation complexity. Close unnecessary applications to free RAM. Lower the physics update rate in the world file. Consider using a lighter robot model."
    },
    {
        "topic": "Gazebo crash on startup",
        "content": "If Gazebo crashes on startup, update GPU drivers. Try running with software rendering: export LIBGL_ALWAYS_SOFTWARE=1. Kill existing Gazebo processes with pkill -f gz. Clear Gazebo cache with rm -rf ~/.gz."
    },
    {
        "topic": "Gazebo Sim 8 ROS2 Jazzy",
        "content": "Gazebo Sim 8 (Harmonic) is the supported version for ROS2 Jazzy. Install with sudo apt install ros-jazzy-ros-gz. Use ros_gz_bridge for topic bridging between Gazebo and ROS2. Old gazebo_ros_pkgs are not compatible."
    },
    {
        "topic": "Gazebo Sim 8 bridge topics",
        "content": "In Gazebo Sim 8 with ROS2 Jazzy, use ros_gz_bridge to bridge topics. Example: ros2 run ros_gz_bridge parameter_bridge /scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan. Bridge must be running for topics to appear in ROS2."
    },
    {
        "topic": "Gazebo Sim 8 camera plugin",
        "content": "In Gazebo Sim 8, use gz::sim::systems::Camera plugin for camera sensors. Bridge camera topics with ros_gz_bridge. Use /camera/image topic in ROS2. Install ros-jazzy-ros-gz-sim for Gazebo Sim 8 support."
    },
    {
        "topic": "Gazebo Sim 8 physics",
        "content": "Gazebo Sim 8 uses the Bullet or DART physics engine. Configure physics in the world SDF file. Set max_step_size to 0.001 for accurate simulation. Real time factor below 1.0 means simulation is running slow."
    },
    {
        "topic": "Gazebo headless mode",
        "content": "Run Gazebo in headless mode without GUI using gz sim -s world.sdf. This saves resources when GUI is not needed. Use for automated testing or when running on a server without display."
    },

    # --- LIDAR ---
    {
        "topic": "LiDAR showing inf values",
        "content": "LiDAR showing inf values means no obstacles are detected in sensor range. This is normal in an empty Gazebo world. The sensor is working correctly. Add obstacles in Gazebo to see real range values."
    },
    {
        "topic": "LiDAR not publishing",
        "content": "If LiDAR is not publishing on /scan topic, check that the robot is spawned in Gazebo. Verify ros_gz_bridge is running and bridging the scan topic. Check with ros2 topic hz /scan to see publish rate."
    },
    {
        "topic": "LiDAR data incorrect",
        "content": "If LiDAR data seems incorrect, check the sensor configuration in the URDF. Verify the scan range parameters like range_min and range_max. Make sure the sensor frame is correctly defined in TF tree."
    },
    {
        "topic": "LiDAR scan frequency too low",
        "content": "If LiDAR scan frequency is too low, check the sensor update rate in URDF or SDF file. Increase the update_rate parameter. Make sure the simulation is not running slower than real time."
    },
    {
        "topic": "LiDAR 3D pointcloud",
        "content": "For 3D LiDAR pointcloud data, use /points topic instead of /scan. Install ros-jazzy-sensor-msgs. Use rviz2 to visualize pointcloud with PointCloud2 display. 3D LiDAR uses more bandwidth than 2D."
    },
    {
        "topic": "LiDAR obstacle detection",
        "content": "For obstacle detection with LiDAR, use the /scan topic with range values. Values less than range_max indicate obstacles. Filter inf values as they mean no obstacle detected. Use Nav2 costmap for automatic obstacle mapping."
    },

    # --- NAVIGATION ---
    {
        "topic": "Nav2 navigation not working",
        "content": "If Nav2 is not working, make sure to launch navigation with ros2 launch nav2_bringup navigation_launch.py. Check that the map is provided and amcl localization is running. Verify /scan and /odom topics are publishing."
    },
    {
        "topic": "Nav2 goal rejected",
        "content": "If Nav2 rejects a navigation goal, check that the goal is within the map bounds. Make sure the robot is localized correctly with AMCL. Verify the costmap is properly configured. Check Nav2 logs for specific error."
    },
    {
        "topic": "Nav2 robot stuck during navigation",
        "content": "If robot gets stuck during navigation, check for obstacles in the costmap. Clear the costmap with ros2 service call /clear_costmaps. Adjust the recovery behaviors in Nav2 parameters. Check inflation radius settings."
    },
    {
        "topic": "Nav2 map not loading",
        "content": "If Nav2 map is not loading, check the map file path in the launch file. Make sure the map yaml file and pgm file are in the same directory. Verify map_server node is running with ros2 node list."
    },
    {
        "topic": "AMCL localization not working",
        "content": "If AMCL localization is not working, make sure the map is loaded. Check that /scan topic is publishing. Set initial pose in RViz or with ros2 topic pub. Increase the number of particles in AMCL parameters."
    },
    {
        "topic": "Nav2 costmap not updating",
        "content": "If Nav2 costmap is not updating, check that sensor topics are publishing. Verify costmap parameters include correct sensor sources. Make sure observation sources are correctly configured in nav2_params.yaml."
    },
    {
        "topic": "Nav2 Jazzy configuration",
        "content": "Nav2 in ROS2 Jazzy uses updated parameter names. Install with sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup. Use nav2_params.yaml for configuration. BT Navigator uses behavior trees for complex navigation."
    },
    {
        "topic": "Nav2 behavior tree",
        "content": "Nav2 uses behavior trees for navigation logic. Default BT XML files are in nav2_bt_navigator package. Customize behavior by creating new BT XML files. Use NavigateToPose action for simple point-to-point navigation."
    },
    {
        "topic": "Nav2 speed limits",
        "content": "To set robot speed limits in Nav2, configure max_vel_x, max_vel_y, max_vel_theta in nav2_params.yaml. Set min_vel_x for minimum forward speed. Use velocity smoother plugin for smooth motion."
    },
    {
        "topic": "Nav2 recovery behaviors",
        "content": "Nav2 recovery behaviors activate when robot is stuck. Default recoveries are spin, backup, and wait. Configure in nav2_params.yaml under recoveries_server. Disable problematic recoveries if they cause issues."
    },
    {
        "topic": "Nav2 global planner",
        "content": "Nav2 uses NavFn or Smac planner for global path planning. Configure planner_server in nav2_params.yaml. NavFn is simpler, Smac supports Hybrid-A* for car-like robots. Choose based on robot kinematics."
    },
    {
        "topic": "Nav2 local planner",
        "content": "Nav2 uses DWB or MPPI controller for local path following. DWB is the default dynamic window approach controller. MPPI uses model predictive path integral for smoother motion. Configure in controller_server params."
    },

    # --- TF AND TRANSFORMS ---
    {
        "topic": "TF tree empty or missing transforms",
        "content": "If TF tree is empty, check that robot_state_publisher is running. Make sure the URDF is loaded correctly. Source the workspace and relaunch. Use ros2 run tf2_tools view_frames to visualize the TF tree."
    },
    {
        "topic": "TF transform lookup failed",
        "content": "If TF transform lookup fails, check that both frames exist in the TF tree. Make sure robot_state_publisher and any static transform publishers are running. Check for timing issues with ros2 run tf2_tools tf2_echo frame1 frame2."
    },
    {
        "topic": "TF extrapolation error",
        "content": "If you see TF extrapolation errors, check for clock synchronization issues. Make sure /clock topic is publishing in simulation. Set use_sim_time to true for all nodes in simulation with --ros-args -p use_sim_time:=true."
    },
    {
        "topic": "Static transform publisher",
        "content": "To publish a static transform in ROS2 Jazzy, use ros2 run tf2_ros static_transform_publisher x y z rx ry rz rw parent_frame child_frame. Or use StaticTransformBroadcaster in Python code."
    },
    {
        "topic": "TF2 buffer lookup",
        "content": "To lookup transforms in ROS2 Python, create a tf2_ros.Buffer and TransformListener. Use buffer.lookup_transform(target_frame, source_frame, rclpy.time.Time()). Handle tf2_ros.LookupException for missing transforms."
    },

    # --- ODOMETRY ---
    {
        "topic": "Odometry not updating",
        "content": "If odometry is not updating, check that the robot simulation is running in Gazebo. Verify /odom topic is publishing with ros2 topic hz /odom. Make sure ros_gz_bridge is running to bridge Gazebo and ROS2 topics."
    },
    {
        "topic": "Odometry drift",
        "content": "Odometry drift is normal over time due to accumulated errors. Use AMCL or other localization methods to correct drift. Consider using sensor fusion with IMU data using robot_localization package."
    },
    {
        "topic": "Robot position not accurate",
        "content": "If robot position is not accurate, check odometry calibration. Use AMCL for map-based localization. Verify wheel encoder parameters in the robot configuration. Consider using external localization sensors."
    },
    {
        "topic": "Robot localization package",
        "content": "Use robot_localization package for sensor fusion in ROS2 Jazzy. Install with sudo apt install ros-jazzy-robot-localization. Fuses IMU and odometry data using Extended Kalman Filter. Configure in ekf.yaml file."
    },

    # --- GENERAL ROBOT ISSUES ---
    {
        "topic": "Robot stuck or not responding",
        "content": "If the robot is stuck, check active nodes with ros2 node list. Restart the simulation by killing and relaunching Gazebo. Check if /cmd_vel has active publishers. Try sending manual velocity commands with ros2 topic pub."
    },
    {
        "topic": "cmd_vel not working",
        "content": "If /cmd_vel commands are not working, check that the robot controller is running. Verify the topic name matches what the robot expects. Make sure velocity values are within the robot limits. Check for any emergency stop signals."
    },
    {
        "topic": "IMU data not publishing",
        "content": "If IMU data is not publishing on /imu topic, check that the IMU sensor is defined in the robot URDF. Verify ros_gz_bridge is bridging the IMU topic. Check with ros2 topic hz /imu to see publish rate."
    },
    {
        "topic": "Joint states not publishing",
        "content": "If joint states are not publishing, check that joint_state_publisher is running. Verify the robot URDF has correctly defined joints. Make sure robot_state_publisher is also running alongside joint_state_publisher."
    },
    {
        "topic": "Robot description not loaded",
        "content": "If robot description is not loaded, check that robot_state_publisher is running with the correct URDF. Verify /robot_description topic is publishing. Make sure the URDF file path is correct in the launch file."
    },
    {
        "topic": "Emergency stop robot",
        "content": "To emergency stop a ROS2 robot, publish zero velocity to /cmd_vel: ros2 topic pub /cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.0}, angular: {z: 0.0}}'. Or kill the teleop node with Ctrl+C."
    },
    {
        "topic": "Robot velocity commands",
        "content": "To send velocity commands to a ROS2 robot manually, use ros2 topic pub /cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.5}, angular: {z: 0.0}}' --once. This moves the robot forward at 0.5 m/s."
    },
    {
        "topic": "Multiple robots ROS2",
        "content": "To run multiple robots in ROS2, use namespaces for each robot. Launch each robot with a unique namespace like /robot1 and /robot2. All topics and nodes will be prefixed with the namespace. Use ROS_DOMAIN_ID to isolate robot networks."
    },
    {
        "topic": "Robot auto detection",
        "content": "To detect what robot is connected in ROS2, check active nodes with ros2 node list and topics with ros2 topic list. Look for robot_state_publisher and /robot_description topic. Parse URDF from /robot_description to identify robot type."
    },

    # --- RVIZ ---
    {
        "topic": "RViz not showing robot",
        "content": "If RViz is not showing the robot, check that robot_state_publisher is running. Set the Fixed Frame to odom or map in RViz. Add a RobotModel display and set the topic to /robot_description."
    },
    {
        "topic": "RViz no map displayed",
        "content": "If RViz is not showing the map, check that map_server is running. Add a Map display in RViz and set the topic to /map. Make sure the map file is loaded correctly by Nav2."
    },
    {
        "topic": "RViz laser scan not visible",
        "content": "If laser scan is not visible in RViz, add a LaserScan display and set topic to /scan. Check the Fixed Frame matches the scan frame_id. Make sure the LiDAR is publishing data."
    },
    {
        "topic": "RViz2 Jazzy",
        "content": "RViz2 is the ROS2 version of RViz. Launch with rviz2 command. Add displays using the Add button. Save configuration as .rviz file. Use ros2 run rviz2 rviz2 -d config.rviz to load saved configuration."
    },

    # --- PERFORMANCE ---
    {
        "topic": "High CPU usage in ROS2",
        "content": "If ROS2 is using high CPU, check for nodes publishing at very high frequencies. Reduce publish rates where possible. Use ros2 topic hz to monitor frequencies. Consider using composable nodes to reduce overhead."
    },
    {
        "topic": "High memory usage",
        "content": "If memory usage is high, check for memory leaks in custom nodes. Reduce the number of running nodes. Lower the history depth of subscriptions. Consider using a lighter simulation or robot model."
    },
    {
        "topic": "Simulation time vs real time",
        "content": "In Gazebo simulation, always use use_sim_time:=true for all nodes. Set the clock source to Gazebo. Make sure /clock topic is being published by Gazebo and bridged to ROS2."
    },

    # --- CODE FIXES ---
    {
        "topic": "create_publisher missing queue size",
        "content": "In ROS2, create_publisher always requires 3 arguments: message type, topic name, and queue size. Correct usage: self.publisher = self.create_publisher(String, 'topic_name', 10). Missing queue_size will cause a TypeError."
    },
    {
        "topic": "create_subscription missing arguments",
        "content": "In ROS2, create_subscription requires 4 arguments: message type, topic name, callback function, and queue size. Correct usage: self.subscription = self.create_subscription(String, 'topic', self.callback, 10)."
    },
    {
        "topic": "rclpy.spin missing node argument",
        "content": "In ROS2, rclpy.spin() requires the node object as argument. Wrong: rclpy.spin(). Correct: rclpy.spin(node). Same for rclpy.spin_once(node)."
    },
    {
        "topic": "rclpy.init missing args",
        "content": "In ROS2, rclpy.init() should be called with args=None. Correct usage: rclpy.init(args=None). Or pass sys.argv: rclpy.init(args=sys.argv)."
    },
    {
        "topic": "Node super().__init__ missing name",
        "content": "In ROS2, when creating a Node class, super().__init__() must include the node name string. Wrong: super().__init__(). Correct: super().__init__('my_node_name')."
    },
    {
        "topic": "msg.data wrong attribute",
        "content": "In ROS2 std_msgs, String message uses .data attribute not .text or .message. Wrong: msg.text = 'hello'. Correct: msg.data = 'hello'. For Int32: msg.data = 42."
    },
    {
        "topic": "timer callback name mismatch",
        "content": "In ROS2, the timer callback name passed to create_timer must exactly match the method name. Wrong: self.create_timer(0.5, self.timerCallback) with method def timer_callback. Correct: make sure both names match exactly."
    },
    {
        "topic": "missing import rclpy",
        "content": "Every ROS2 Python node must import rclpy and the Node class. Required imports: import rclpy, from rclpy.node import Node. Also import message types like: from std_msgs.msg import String."
    },
    {
        "topic": "publisher publish wrong usage",
        "content": "In ROS2, to publish a message, create the message object first then publish. Correct pattern: msg = String(); msg.data = 'hello'; self.publisher.publish(msg). Do not pass raw strings directly to publish()."
    },
    {
        "topic": "ROS2 node not shutting down cleanly",
        "content": "In ROS2, always call rclpy.shutdown() after rclpy.spin() ends. Use try/finally to ensure cleanup. Pattern: try: rclpy.spin(node) finally: node.destroy_node(); rclpy.shutdown()."
    },
    {
        "topic": "ROS2 Python node template",
        "content": "Basic ROS2 Python node template: import rclpy; from rclpy.node import Node; class MyNode(Node): def __init__(self): super().__init__('node_name'); def main(args=None): rclpy.init(args=args); node = MyNode(); rclpy.spin(node); node.destroy_node(); rclpy.shutdown()."
    },
    {
        "topic": "ROS2 launch file Python",
        "content": "ROS2 Jazzy launch files use Python. Basic template: from launch import LaunchDescription; from launch_ros.actions import Node; def generate_launch_description(): return LaunchDescription([Node(package='pkg', executable='node', name='node_name')])"
    },
    {
        "topic": "ROS2 custom message type",
        "content": "To create custom ROS2 messages, create a .msg file in a msg/ directory. Add rosidl_default_generators as dependency in package.xml. Build with colcon build. Import with from package_name.msg import MessageName."
    },
    {
        "topic": "ROS2 service server",
        "content": "To create a ROS2 service server: self.srv = self.create_service(ServiceType, 'service_name', self.callback). Callback receives request and response objects. Return the response object from callback."
    },
    {
        "topic": "ROS2 service client",
        "content": "To create a ROS2 service client: self.client = self.create_client(ServiceType, 'service_name'). Call with self.client.call_async(request). Use rclpy.spin_until_future_complete to wait for response."
    },
    {
        "topic": "ROS2 QoS profile",
        "content": "To set QoS profile in ROS2: from rclpy.qos import QoSProfile, ReliabilityPolicy; qos = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, depth=10); self.publisher = self.create_publisher(String, 'topic', qos)."
    },
    {
        "topic": "ROS2 timer callback",
        "content": "To create a timer in ROS2: self.timer = self.create_timer(timer_period_sec, self.timer_callback). Timer period is in seconds. Use 0.1 for 10Hz, 1.0 for 1Hz. Cancel timer with self.timer.cancel()."
    },
    {
        "topic": "ROS2 parameter declaration",
        "content": "In ROS2 Jazzy, parameters must be declared before use. Use self.declare_parameter('param_name', default_value). Get value with self.get_parameter('param_name').value. Set from command line with --ros-args -p param_name:=value."
    },
    {
        "topic": "ROS2 logging",
        "content": "Use ROS2 logging instead of print for node output. self.get_logger().info('message') for info. self.get_logger().warn('warning') for warnings. self.get_logger().error('error') for errors. Logs appear in terminal and can be recorded."
    },

    # --- SENSORS ---
    {
        "topic": "Camera not publishing",
        "content": "If camera is not publishing, check that the camera plugin is configured in URDF. Verify ros_gz_bridge is bridging camera topics. Check /camera/image topic with ros2 topic hz. Install ros-jazzy-image-transport for compressed images."
    },
    {
        "topic": "Depth camera setup",
        "content": "For depth camera in ROS2 Jazzy, use /depth/image topic for depth data and /depth/points for pointcloud. Install ros-jazzy-depth-image-proc for processing. Use ros2 run depth_image_proc point_cloud_xyz for pointcloud conversion."
    },
    {
        "topic": "IMU sensor fusion",
        "content": "For IMU sensor fusion in ROS2 Jazzy, use robot_localization package. Configure EKF node with IMU and odometry inputs. Set imu0 to /imu topic in ekf.yaml. This improves robot localization accuracy."
    },
    {
        "topic": "GPS sensor ROS2",
        "content": "For GPS in ROS2, use sensor_msgs/NavSatFix message type on /gps/fix topic. Use robot_localization with navsat_transform_node to convert GPS to odom. Install ros-jazzy-robot-localization for GPS fusion."
    },
    {
        "topic": "Ultrasonic sensor ROS2",
        "content": "For ultrasonic sensors in ROS2, publish on sensor_msgs/Range message type. Set radiation_type to ULTRASOUND. Set min_range and max_range in meters. Topic name convention is /ultrasonic or /range."
    },

    # --- DOCKER AND DEPLOYMENT ---
    {
        "topic": "Docker ROS2 setup",
        "content": "To run ROS2 in Docker, use official ROS2 Docker images from docker.io/ros. Use ros:jazzy for ROS2 Jazzy base image. Mount workspace with -v /path/to/ws:/ros2_ws. Source setup.bash in Dockerfile with RUN echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc."
    },
    {
        "topic": "Docker network ROS2",
        "content": "For ROS2 nodes to communicate across Docker containers, use --network host mode. Or set ROS_DOMAIN_ID consistently. DDS discovery works best with host networking. Use docker-compose for multi-container ROS2 setups."
    },
    {
        "topic": "ROS2 cloud deployment",
        "content": "To deploy ROS2 AI assistant to cloud, separate the AI component from the robot component. Run AI agent on cloud with API access. Keep robot MCP server local. Use REST API to bridge local robot data to cloud AI."
    },

    # --- DEBUGGING ---
    {
        "topic": "ROS2 debug logging",
        "content": "To enable debug logging in ROS2, add --ros-args --log-level DEBUG when running a node. Or set log level for specific node: --ros-args --log-level node_name:=DEBUG. View logs with ros2 run rqt_console rqt_console."
    },
    {
        "topic": "ROS2 node graph",
        "content": "To visualize ROS2 node graph, use rqt_graph: ros2 run rqt_graph rqt_graph. This shows all nodes and their topic connections. Useful for debugging communication issues between nodes."
    },
    {
        "topic": "ROS2 topic echo filtering",
        "content": "To filter ros2 topic echo output, use --no-arr to hide arrays or --once to get single message. Use --field to show specific fields: ros2 topic echo --field pose.position /odom. Useful for large messages like LiDAR scans."
    },
    {
        "topic": "ROS2 introspection tools",
        "content": "ROS2 Jazzy introspection tools: ros2 node info /node_name shows subscriptions and publishers. ros2 topic info /topic_name shows message type and QoS. ros2 service type /service_name shows service type."
    },
    {
        "topic": "ROS2 rosdep install",
        "content": "To install all dependencies for a ROS2 workspace, run rosdep install --from-paths src --ignore-src -r -y from workspace root. Run rosdep update first if packages are not found. This installs all package.xml dependencies."
    },

    # --- MULTI ROBOT ---
    {
        "topic": "Multi robot namespace",
        "content": "For multi-robot ROS2 systems, use namespaces: ros2 launch package launch_file.py namespace:=robot1. All topics will be prefixed: /robot1/cmd_vel, /robot1/odom. Use namespace parameter in Node() launch action."
    },
    {
        "topic": "Multi robot communication",
        "content": "For multiple robots to communicate in ROS2, they must share the same ROS_DOMAIN_ID. Use namespaces to avoid topic conflicts. Use ros2 topic list to see all robot topics. Each robot needs unique node names."
    },
    {
        "topic": "Robot fleet management",
        "content": "For robot fleet management in ROS2, use a central coordinator node. Each robot publishes status to /robot_name/status. Coordinator subscribes to all robot statuses. Use action servers for task assignment to individual robots."
    },
]