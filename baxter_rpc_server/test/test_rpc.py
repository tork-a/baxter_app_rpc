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

import unittest

from geometry_msgs.msg import Pose
import rospy

from baxter_app_rcp.sample_rpc import SampleRpcBaxter

PKG = 'baxter_rpc_server'


class TestBaxterRpc(unittest.TestCase):

    def setUp(self):
        self.sample_rpc = SampleRpcBaxter()

    def tearDown(self):
        True

    def test_cartesian_move_left(self):
        '''
        Test criteria: The ROS Service return bool, and True if the internal
                       call finished without issue.
        '''
        self.assertTrue(self.sample_rpc.sample_cartesian_move('left'))

    def test_cartesian_move_right(self):
        '''
        Test criteria: The ROS Service return bool, and True if the internal
                       call finished without issue.
        '''
        self.assertTrue(self.sample_rpc.sample_cartesian_move('right'))

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_rpc', TestBaxterRpc) 
