#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

# Basic definition
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

# Move to the target pose
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 0.0
pose_target.position.x = -3.32658241794e-05
pose_target.position.y = 0.707339309732
pose_target.position.z = 0.706874174954
group.set_pose_target(pose_target)
plan1 = group.go(wait = True)
# group.stop()
plan1 = group.plan()
group.execute(plan1, wait = True)
group.clear_pose_targets()

print "Finished the first pose"
rospy.sleep(10.0)

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.54156925114e-05
pose_target.position.x = 3.34980148704e-05
pose_target.position.y = 0.707111290638
pose_target.position.z = 0.707102270745
group.set_pose_target(pose_target)
plan2 = group.go(wait = True)
group.stop()
plan2 = group.plan()
group.execute(plan2, wait = True)
group.clear_pose_targets()



