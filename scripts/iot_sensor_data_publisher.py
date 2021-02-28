#!/usr/bin/env python3
import rospy
from ros_fundamentals.msg import IoTSensor
import random


def publish():
    # name is topic name, type of the message to be published is String
    publisher = rospy.Publisher(name="iot_sensor_data_topic", data_class=IoTSensor, queue_size=10)
    # name is node name
    rospy.init_node(name="iot_sensor_data_publisher", anonymous=True)
    # Hz => msg/sec ex: 10 msg/sec
    rate = rospy.Rate(0.5)

    idx = 0
    while not rospy.is_shutdown():
        # create IoTSensor object
        iot_sensor_data = IoTSensor()
        iot_sensor_data.name = "temp_humid_iot_sensor"
        iot_sensor_data.id = 99
        iot_sensor_data.temperature = 3.26 * random.randint(5, 15)
        iot_sensor_data.humidity = 2.26 * random.randint(1, 5)
        rospy.loginfo(iot_sensor_data)
        publisher.publish(iot_sensor_data)
        rate.sleep()
        idx += 1

if __name__ == "__main__":
    try:
        publish()
    except rospy.ROSInterruptException as exc:
        rospy.logerr("Encountered exception: {}".format(exc))
