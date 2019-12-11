#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np

# Basic definition
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

# 1. Move to the target pose based on the joint coordinates
pose_1 = [8.766081638696851e-05, -0.30412391442294173, -0.10924829317510322, -0.17492873280315546, 7.950723048148287e-05, 0.5882364992499817]
print "------------- Planning to the pose 2 --------------"
group.clear_pose_targets()
group_variable_values = group.get_current_joint_values()
group_variable_values[0] = pose_1[0]
group_variable_values[1] = pose_1[1]
group_variable_values[2] = pose_1[2]
group_variable_values[3] = pose_1[3]
group_variable_values[4] = pose_1[4]
group_variable_values[5] = pose_1[5]
group.set_joint_value_target(group_variable_values)
plan1 = group.plan()
group.execute(plan1, wait = True)
# The FK and jacobian information 
print "Pose of the end effector (Joint 2):"
print group.get_current_pose()
print "rpy of the end effector (Joint 2):"
print group.get_current_rpy()
print "Jacobian of the robot (Joint 2):"
joints = group.get_current_joint_values()
print group.get_jacobian_matrix(joints)
J = group.get_jacobian_matrix(joints)
print "The shape of the Jacobian matrix is "
print J.shape
np.save("Pose_2.npy", J)
group.stop()
group.clear_pose_targets()
rospy.sleep(2)

# 2. Move to the second position
pose_2 = [4.018215740774515e-05, -0.9092939328199339, 0.6468498754343582, -0.9572414918873298, -3.1893106040647604e-05, 1.2195654818647514]
print "----------- Planning to the pose 3 ----------------"
group.clear_pose_targets()
group_variable_values = group.get_current_joint_values()
group_variable_values[0] = pose_2[0]
group_variable_values[1] = pose_2[1]
group_variable_values[2] = pose_2[2]
group_variable_values[3] = pose_2[3]
group_variable_values[4] = pose_2[4]
group_variable_values[5] = pose_2[5]
group.set_joint_value_target(group_variable_values)
plan2 = group.plan()
group.execute(plan2, wait = True)
# The FK and jacobian information 
print "Pose of the end effector (Joint 3):"
print group.get_current_pose()
print "rpy of the end effector (Joint 3):"
print group.get_current_rpy()
print "Jacobian of the robot (Joint 3):"
joints = group.get_current_joint_values()
print group.get_jacobian_matrix(joints)
J = group.get_jacobian_matrix(joints)
print "The shape of the Jacobian matrix is "
print J.shape
np.save("Pose_3.npy", J)
group.stop()
group.clear_pose_targets()
rospy.sleep(2)

# 3. Move back to position 3
pose_3 = [8.766081638696851e-05, -0.30412391442294173, -0.10924829317510322, -0.17492873280315546, 7.950723048148287e-05, 0.5882364992499817]
print "------- Planning to the pose 2 ---------------"
group.clear_pose_targets()
group_variable_values = group.get_current_joint_values()
group_variable_values[0] = pose_3[0]
group_variable_values[1] = pose_3[1]
group_variable_values[2] = pose_3[2]
group_variable_values[3] = pose_3[3]
group_variable_values[4] = pose_3[4]
group_variable_values[5] = pose_3[5]
group.set_joint_value_target(group_variable_values)
plan3 = group.plan()
group.execute(plan3, wait = True)
group.stop()
group.clear_pose_targets()
rospy.sleep(2)

# Move back to the initial positions
pose_4 = [6.622498114593327e-05, -2.7647355617955332e-05, -4.959623068571091e-05, -8.290793648920954e-05, 3.643605378456415e-05, 2.5445600273087623e-05]
print "---------- Planning to the pose 1 ---------------"
group.clear_pose_targets()
group_variable_values = group.get_current_joint_values()
group_variable_values[0] = pose_4[0]
group_variable_values[1] = pose_4[1]
group_variable_values[2] = pose_4[2]
group_variable_values[3] = pose_4[3]
group_variable_values[4] = pose_4[4]
group_variable_values[5] = pose_4[5]
group.set_joint_value_target(group_variable_values)
plan4 = group.plan()
group.execute(plan4, wait = True)
# The FK and jacobian information 
print "Pose of the end effector (Joint 1):"
print group.get_current_pose()
print "rpy of the end effector (Joint 1):"
print group.get_current_rpy()
print "Jacobian of the robot (Joint 1):"
joints = group.get_current_joint_values()
print group.get_jacobian_matrix(joints)
J = group.get_jacobian_matrix(joints)
print "The shape of the Jacobian matrix is "
print J.shape
np.save("Pose_1.npy", J)
group.stop()
group.clear_pose_targets()
rospy.sleep(2)

moveit_commander.roscpp_shutdown()

