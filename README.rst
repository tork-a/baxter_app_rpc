-----------------------------------------------------------------
baxter_rpc_server (RPC (Remote Procedure Call)) ROS package
-----------------------------------------------------------------

Install
-------

Make sure `baxter_rpc_msgs` and `tork_rpc_util` packages are under you catkin workspace and build them by something like:

::

  sudo apt-get install python-catkin-tools python-rosdep python-wstool
  mkdir -p ~/cws_rpc/src && cd ~/cws_rpc
  wstool init src
  wstool merge -t src https://raw.githubusercontent.com/tork-a/baxter_app_rpc/master/.rosinstall
  wstool update -t src
  rosdep install -r -y --from-paths src --ignore-src
  catkin build
  source devel/setup.bash

Usage
----------------------------

You simply need to (1) run RPC server and you're ready to (2) execute your commands.

Run RPC server
===============

Run RPC server that starts ROS nodes for RPC.

Or run in simulation mode if you're not working with a real robot. This starts `Gazebo` and `RViz` that use up lots of computer resource.::

  roslaunch baxter_rpc_server rpc.launch        (Real robot)

  roslaunch baxter_rpc_server rpc_sim.launch    (simulation)


Execute your command
==============================

RPC invocations defined in this package are normal ROS Service (+ some Actions). So call them by the ROS Service manner.

You can get an idea by seeing the sample script on `ipython` terminal, which can be run as::

  ipython -i `rospack find baxter_rpc_server`/script/samplescript_baxter_rpc.py

Tech support
--------------

Search existing issues, submit a ticket at `GitHub <https://github.com/tork-a/baxter_app_rpc/issues>`_.

Troubleshooting
==================

IK failure with "[/ExternalTools/left/PositionKinematicsNode/IKService] responded with an error"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure Gazebo launch is run from a terminal where `baxter.sh sim` was already run properly.

EoF
