#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:27:05 2021

@author: palash
"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(dt):
    print('..................................')
    print('Range data at 0 degree:',dt.ranges[0])
    print('Range data at 15 degree:',dt.ranges[15])
    print('Range data at 345 degree:',dt.ranges[345])
    print('..................................')
    thr = 1
    
    if dt.ranges[0]>thr and dt.ranges[15]>thr and dt.ranges[345>thr]:
        move.linear.x = 0.5
        move.angular.z = 0
    else:
        move.linear.x = 0
        move.angular.z = 0.5
        if dt.ranges[0]>thr and dt.ranges[15]>thr and dt.ranges[345>thr]:
           move.linear.x = 0.5
           move.angular.z = 0
    pub.publish(move)
    
move = Twist()
rospy.init_node("obstacle_avoidance", anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)

sub= rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()

        
