-----------------------------------------------------------------
tork_rpc_util (RPC (Remote Procedure Call)) ROS package
-----------------------------------------------------------------

Insall
------

Mkae sure `baxter_rpc_msgs` and `tork_rpc_util` packages are under you catkin workspace and build them by something like:

::

  mv baxter_rpc_msgs tork_rpc_util %YOUR_CATKIN_WS%/src
  cd %YOUR_CATKIN_WS%
  rosdep install -r -y --from-paths src --ignore-src
  catkin build tork_rpc_util
  source devel/setup.bash

Run RPC nodes on simulation
----------------------------

1. Run HSR Gazebo simulation package, by something like:

::

  roslaunch hsrb_gazebo_launch hsrb_empty_world.launch paused:=false

2. Run RPC server that starts ROS nodes for RPC.

::

  rosrun tork_rpc_util rpc_servers_handler_script.py

Run sample remote invocations
------------------------------

1. Start sample script on `ipython` terminal.

::

  ipython -i `rospack find tork_rpc_util`/script/sample_script.py

2. Following commands are available on the ipython terminal.

* sample_rpc.sample_move_to_neutral: ROS Action
* sample_rpc.sample_omni_base_go: ROS Action
* sample_rpc.sample_omni_base_get_pose: ROS Service

Troubleshooting
---------------

IK failure with "[/ExternalTools/left/PositionKinematicsNode/IKService] responded with an error"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure Gazebo launch is run from a terminal where `baxter.sh sim` was already run properly.

EoF
