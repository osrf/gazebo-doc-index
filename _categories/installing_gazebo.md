---
# Contribution guidelines:
# https://github.com/osrf/gz-bigindex/blob/master/CONTRIBUTING.md 

title: "Installing the Gazebo simulator"
desc: "Links related to the Gazebo's installation instructions for different supported platforms"
subcategories: 
  - title: "Installing on Linux"
    items: 
      - title: 'One line installation'
        url: 'http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install#Defaultinstallation:one-liner'
        desc: 'Short command to run in your terminal to install the latest Gazebo for any linux distribution' 
        star: true

      - title: 'Ubuntu: Choosing your package repositories'
        url: 'http://gazebosim.org/tutorials?tut=ros_wrapper_versions&cat=connect_ros#Important!simpleanalysisforaquickandcorrectdecision'
        desc: 'Gazebo can be installed from different repositories. Special attention for ROS users.'
        star: true

      - title: 'Ubuntu: Packages installation'
        url: 'http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install#Alternativeinstallation:step-by-step'
        desc: 'Traditional steps to configure a repository and step-by-step installation instructions for the Ubuntu binaries using apt-get.'
        star: true

      - title: 'Ubuntu: Prereleases/nightly packages installation'
        url: 'http://gazebosim.org/tutorials?tut=install_unstable&cat=install'
        desc: 'Experimental packages created from development branches still unreleased in official releases'
        star: false

      - title: 'Debian: Packages installation'
        url: 'http://gazebosim.org/tutorials?tut=install_other_linux&cat=install#Debian'
        desc: 'How to install Gazebo on Debian using .deb packages'
        star: true
      
      - title: 'Debian: Installing gazebo7 on Jessie'
        url: 'http://answers.gazebosim.org/question/13031/installing-gazebo-in-debian-jessie/'
        desc: 'How to install Gazebo using the package manager in other Linux distributions'
        star: false

      - title: 'Fedora, Arch, Gentoo installations'
        url: 'http://gazebosim.org/tutorials?tut=install_other_linux&cat=install#Debian'
        desc: 'Instructions to install Gazebo7 on Debian Jessie'
        star: false
      
      - title: ''
        url: 'http://gazebosim.org/tutorials?tut=install_from_source&cat=install#InstallGazebofromsource%28UbuntuandMac%29'
        desc: 'How to compile gazebo from source on a Linux distribution.'
        star: false

      - title: 'Docker Gazebo images'
        url: 'https://hub.docker.com/_/gazebo/'
        desc: 'Lightweight virtualized containers with gazebo preinstalled'
        star: false

      - title: 'Gazebo Changelog'
        url: 'https://bitbucket.org/osrf/gazebo/src/default/Changelog.md'
        desc: 'New features, bugfixes and changes between Gazebo versions'
        star: false

  - title: "Installing on MacOSX"
    items:
      - title: 'One line installation'
        url: 'http://gazebosim.org/tutorials?tut=install_on_mac&cat=install#Defaultinstallation:one-liner'
        desc: 'Short command to run in your terminal to install Gazebo on Mac'
        star: true

      # - title: 'Supported OSX versions'
      #   url: 'http://answers.gazebosim.org/question/TODO'
      #   desc: 'Which OSX versions are supported by Gazebo'
      #   star: true

      - title: 'Brew installation step by step'
        url: 'http://gazebosim.org/tutorials?tut=install_on_mac&cat=install#Alternativeinstallation:step-by-step'
        desc: 'Guide to go through all the steps to install Gazebo using the Brew package manager'
        star: false

      - title: 'Brew Gazebo repository'
        url: 'https://github.com/osrf/homebrew-simulation'
        desc: 'Github repo containing the brew metadata about all gazebo related packages.'
        star: false

      # - title: 'Gazebo installer for OSX (in progress)'
      #   url: 'http://answers.gazebosim.org/question/TODO'
      #   desc: 'Roadmap to implement a Gazebo installer for OSX'
      #   star: false

      - title: 'Using ROS and Gazebo on MacOSX'
        url: 'http://wiki.ros.org/jade/Installation/OSX/Homebrew/Source'
        desc: 'Instructions to install ROS + Gazebo on MacOSX'
        star: false

      - title: 'Compiling Gazebo from source on Mac'
        url: 'http://wiki.ros.org/jade/Installation/OSX/Homebrew/Source'
        desc: 'How to compile Gazebo from source on a Mac distribution'
        star: false

  - title: "Gazebo + ROS installation on Ubuntu Linux"
    items:
      - title: 'Choosing the right repositories for Gazebo/ROS'
        url: 'http://gazebosim.org/tutorials?tut=ros_wrapper_versions&cat=connect_ros'
        desc: 'Analysis of Gazebo versions for ROS + Gazebo integration .'
        star: true

      - title: 'The version fully supported by ROS Indigo, Jade or Kinetic'
        url: 'http://gazebosim.org/tutorials?tut=ros_wrapper_versions&cat=connect_ros#UsingthedefaultGazeboversionforaROSdistribution'
        desc: 'Which is the Gazebo version fully supported by all binary packages distributed by ROS'
        star: true
        
      - title: 'Using latest Gazebo with ROS'
        url: 'http://gazebosim.org/tutorials?tut=ros_wrapper_versions&cat=connect_ros#UsingaspecificGazeboversionwithROS'
        desc: 'Target for advanced users: how to use latest Gazebo version with the different ROS distributions'
        star: true

  - title: "Installing on Windows"
    items:
      - title: 'Windows7 + MSVC12 installation'
        url: 'http://gazebosim.org/tutorials?tut=install_on_windows&cat=install'
        desc: 'Instructions to build gazebo in Windows7 using MSVC12'
        star: true

      # - title: 'MSVC versions different than MSVC12'
      #   url: 'http://answers.gazebosim.org/question/TODO' # todo
      #   desc: 'Status of the support for different versions of Microsoft Visual Studio C++ compiler'
      #   star: false

      # - title: 'Windows10 or other Windows versions installation'
      #   url: 'http://answers.gazebosim.org/question/TODO' # todo
      #   desc: 'Status of the support for different versions of Microsoft Windows, particularly Windows 10.'
      #   star: false


---
