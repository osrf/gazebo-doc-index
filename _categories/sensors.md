---
# Contribution guidelines:
# https://github.com/osrf/gz-bigindex/blob/master/CONTRIBUTING.md 

title: "Sensors: The sensor catalogue"
desc: "How to add already implemented sensors (camera, lasers, IMU, ...) to the gazebo models."
subcategories: 
  - title: "Altimeter Gazebo sensor"
    items: 
      - title: 'Basic shapes in Gazebo simulator'
        url: 'http://gazebosim.org/tutorials?tut=build_world&cat=build_world#AddingSimpleShapes'
        desc: 'How to add simple shapes to the world'
        star: true

      - title: 'Camera Gazebo sensor'
        url: 'http://gazebosim.org/tutorials?tut=camera_save&cat=sensors#Createaworldwithacamera'
        desc: 'How to insert and use a simulated camera in Gazebo'
        star: true

      - title: 'Camera sensor with distorsion in Gazebo'
        url: 'http://gazebosim.org/tutorials?tut=camera_distortion'
        desc: 'How to simulate different camera distorsions in Gazebo'
        star: true

      - title: 'Contact Gazebo sensor'
        url: 'http://gazebosim.org/tutorials?tut=contact_sensor'
        desc: 'Simulate a contact sensor that detects collisions between two object and reports the location of the contact associated forces.'
        star: true
  
  - title: "Sensors integrated with ROS (gazebo_ros_pkgs)"
    items: 
      - title: 'Differences between the gazebo_ros_pkgs sensors and gazebo native sensors'
        url: 'https://github.com/ros-simulation/gazebo_ros_pkgs/blob/kinetic-devel/SENSORS.md'
        desc: 'How are gazebo_ros_pkgs sensors different from the native Gazebo sensors and why is it recommended to use them in ROS'
        star: true
        
      - title: 'Camera sensor in gazebo_ros_pkgs'
        url: 'http://gazebosim.org/tutorials?tut=ros_gzplugins#Camera'
        desc: 'ROS implementation for the Gazebo camera sensor simulaton'
        star: true

      - title: 'GPU Laser sensor in gazebo_ros_pkgs'
        url: 'http://gazebosim.org/tutorials?tut=ros_gzplugins#GPULaser'
        desc: 'ROS implementation for the GPU Laser sensor simulaton'
        star: true

        
---
