#!/usr/bin/env python3
import rospy
from ros_fundamentals.msg import IoTSensor

def subscribe():
    rospy.init_node("iot_sensor_data_subscriber", anonymous=True)
    rospy.Subscriber(name="iot_sensor_data_topic", data_class=IoTSensor, callback=logger)

    # listen forever until interrupted
    rospy.spin()

def logger(sensor_data):
    rospy.loginfo("New sensor data received = {}".format(sensor_data))

if __name__ == "__main__":
    subscribe()