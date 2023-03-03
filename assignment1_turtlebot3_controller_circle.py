#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

class control:
    def __init__(self):
        rospy.init_node("turtlebot3_control", anonymous=True)
        self.twist=Twist()
        self.pub1=rospy.Publisher("/cmd_vel", Twist , queue_size=10)
        self.pub2=rospy.Publisher("/turtle1/cmd_vel", Twist , queue_size=10)       
        self.rate=rospy.Rate(10)
        
    def circle(self):
        self.twist.linear.x=4
        self.twist.angular.z=4

    def controller(self):
        while not rospy.is_shutdown():
            self.circle()        
            rospy.loginfo("sent")
            self.pub1.publish(self.twist)
            self.pub2.publish(self.twist)
            self.rate.sleep()
    

if __name__ == '__main__':
    con = control()
    con.controller()