#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

# Basic Definition
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")

# Move to the first pose

# Move to the second pose

# Move back to the first pose

# Move back to the initial pose

# Output the parameters
# print "Reference frame: %s" % group.get_planning_frame()
print "End effector: %s" % group.get_end_effector_link()
# print "Robot Groups:"
# print robot.get_group_names()
# print "Current Joint Values:"
joints = group.get_current_joint_values()
# print group.get_current_joint_values()
print "Current pose of the end effector:"
# print group.get_current_pose()
P = group.get_current_pose() 
print type(P)

print "Current rpy of the end effector:"
# print group.get_current_rpy()
rpy = group.get_current_rpy()
print type(rpy)

# print "Robot State:"
# print robot.get_current_state()
print "Jacobian matrix"
# print group.get_jacobian_matrix(joints)
J = group.get_jacobian_matrix(joints)
print type(J)

moveit_commander.roscpp_shutdown()
