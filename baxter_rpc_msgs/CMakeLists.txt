cmake_minimum_required(VERSION 2.8.3)
project(baxter_rpc_msgs)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  #baxter_core_msgs
  geometry_msgs
  std_msgs
)

add_service_files(DIRECTORY srv)  #FILES MoveToNeutral.action  # Looks like without FILES directive all files found get compiled, which is nice.   

#add_action_files(DIRECTORY action)

generate_messages(DEPENDENCIES
  actionlib_msgs
  #baxter_core_msgs
  geometry_msgs 
  std_msgs
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES baxter_rpc_msgs
    CATKIN_DEPENDS 
      actionlib_msgs
      #baxter_core_msgs
      geometry_msgs 
      std_msgs
#  DEPENDS system_lib
)
