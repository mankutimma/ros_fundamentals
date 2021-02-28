#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber(name="greetings", data_class=String, callback=logger)

    # listen forever until interrupted
    rospy.spin()

def logger(message):
    rospy.loginfo("{} Just heard {}".format(rospy.get_caller_id(),message.data))
    # rospy.loginfo("hi")

if __name__ == "__main__":
    listener()