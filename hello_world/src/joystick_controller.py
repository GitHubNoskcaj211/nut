#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import String

list = [0,0]
def callback(data):
    list[0] = 100*data.axes[1]
    list[1] = 100*data.axes[4]

if __name__ == '__main__':
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(list)
        pub.publish("Left side: "+str(list[0])+" Right Side: "+str(list[1]))
        rate.sleep()
