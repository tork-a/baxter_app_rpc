#!/usr/bin/env python
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

from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)
import rospy

from baxter_rpc_msgs.srv import (
    SolvePositionIkParts
)
from baxter_rpc_server import BaxterRpcServer


class SampleRpcBaxter(object):
    '''
    RPC sample methods for Baxter. Intended to be called from main method
    within this same python file.
    '''

    def __init__(self):
        '''        '''
        # Start an action server that handles various ROS Actions.
        rospy.init_node('baxter_rpc_sample')

    def sample_cartesian_move(self, limb):
        '''
        @param limb: 'left' or 'right'
        @rtype: bool
        @return: If the service call returns, true.
        '''
        _srv_name = 'srv_cartesian_move'  # Must be the same name defined in ActionServiceNameDict.
        poses = {
            'left': Pose(
                position=Point(
                    x=0.657579481614,
                    y=0.851981417433,
                    z=0.0388352386502,
                ),
                orientation=Quaternion(
                    x=-0.366894936773,
                    y=0.885980397775,
                    z=0.108155782462,
                    w=0.262162481772,
                ),
            ),
            'right': Pose(
                position=Point(
                    x=0.656982770038,
                    y=-0.852598021641,
                    #z=0.0388609422173,
                    z=0.05,
                ),
                orientation=Quaternion(
                    x=0.367048116303,
                    y=0.885911751787,
                    z=-0.108908281936,
                    w=0.261868353356,
                )
            )
        }
        rospy.loginfo('limb: {}, poses[limb]:\n{}'.format(limb, poses[limb]))

        rospy.wait_for_service(_srv_name)
        try:
            _srv_proxy = rospy.ServiceProxy(_srv_name, SolvePositionIkParts)
            _response = _srv_proxy(limb, poses[limb])
            return _response.result
        except rospy.ServiceException, e:
            raise e
