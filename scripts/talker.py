#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def talker():
    # name is topic name, type of the message to be published is String
    publisher = rospy.Publisher(name="greetings", data_class=String, queue_size=10)
    # name is node name
    rospy.init_node(name="talker", anonymous=True)
    # 1 Hz i.e., 1 msg/sec
    rate = rospy.Rate(1)

    idx = 0
    while not rospy.is_shutdown():
        message = "\"Welcome to ROS Fundamentals #{}\"".format(str(idx))
        rospy.loginfo(message)
        publisher.publish(message)
        rate.sleep()
        idx += 1

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException as exc:
        rospy.logerr("Encountered exception: {}".format(exc))
