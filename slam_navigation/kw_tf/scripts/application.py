#! /usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

rospy.init_node('application', anonymous=True)
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map'
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = 0.0
goal.target_pose.pose.orientation.w = 1.0

client.send_goal(goal)
wait = client.wait_for_result()

goal.target_pose.pose.position.x = -32.3742804141
goal.target_pose.pose.position.y = 9.09303728036
goal.target_pose.pose.orientation.z = -0.937480575189
goal.target_pose.pose.orientation.w = 0.348037600187

client.send_goal(goal)
wait = client.wait_for_result()

goal.target_pose.pose.position.x = -12.5181091306
goal.target_pose.pose.position.y = -21.5963123006
goal.target_pose.pose.orientation.z = 0.155247342451
goal.target_pose.pose.orientation.w = 0.987875631171

client.send_goal(goal)
wait = client.wait_for_result()

goal.target_pose.pose.position.x = -0.513808267324
goal.target_pose.pose.position.y = 0.409438658074
goal.target_pose.pose.orientation.z = -0.117538574262
goal.target_pose.pose.orientation.w = 1.0

client.send_goal(goal)
wait = client.wait_for_result()