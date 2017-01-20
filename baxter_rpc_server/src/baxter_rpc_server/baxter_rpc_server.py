# -*- coding: utf-8 -*-

# Copyright 2016 TORK (Tokyo Opensource Robotics Kyokai Association)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import baxter_interface
from baxter_rpc_msgs.srv import (
    SolvePositionIkParts, SolvePositionIkPartsResponse
)
from geometry_msgs.msg import Pose, Quaternion
import rospy

from rpc_server import ActionServiceInfo, RosRpcServer


class ActionServiceNameDict(object):
    '''
    Static, entity class to hold name for ROS Actions for the robot.
    '''
    cartesian_move = 'srv_cartesian_move'


class BaxterRpcServer(RosRpcServer):

    def __init__(self):
        '''
        @param args: TODO
        '''
        rospy.init_node('baxter_rpc_server')

        # Init baxter_interface classes
        self._limb_left = baxter_interface.Limb('left')
        self._limb_right = baxter_interface.Limb('right')

        self.action_infos = {
            ActionServiceNameDict.cartesian_move: ActionServiceInfo(
                ActionServiceNameDict.cartesian_move, SolvePositionIkParts, self._cb_cartesian_move)
        }
        super(BaxterRpcServer, self).__init__(self.action_infos)

        rospy.loginfo(sys._getframe().f_code.co_name + '__init__ done.')

    def _cb_cartesian_move(self, service_req):
        '''
        Computer IK and set the resulted joint angles to the robot's limb.
        '''
        body_part = service_req.body_part
        rospy.loginfo('IN {} Limb: {}'.format(sys._getframe().f_code.co_name, body_part))
        baxter_interface_bodypart = None
        if body_part == 'left':
            baxter_interface_bodypart = self._limb_left
        elif body_part == 'right':
            baxter_interface_bodypart = self._limb_right
        joint_positions = baxter_interface_bodypart.ik(service_req.pose)
        rospy.loginfo('service_req.pose:\n{}\njoint_positions: {}'.format(service_req.pose,
                                                joint_positions))
        if not joint_positions:
            # TODO Return meaningful error message why service failed.
            return SolvePositionIkPartsResponse(False)

        # Call set joint angles to execute the trajectory.
        baxter_interface_bodypart.set_joint_positions(joint_positions)

        return SolvePositionIkPartsResponse(True)
