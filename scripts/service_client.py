#!/usr/bin/env python3
import rospy
import argparse
from ros_fundamentals.srv import AddTwoIntegers


def main(x, y):
    # wait until service is available. service is name of service
    rospy.wait_for_service(service="addition_service")
    try:
        client = rospy.ServiceProxy(name="addition_service", service_class=AddTwoIntegers)
        rospy.init_node(name="addition_client")
        respone_from_server = client(x, y)
    except rospy.ServiceException as exc:
        rospy.loginfo("Service call failed with exception: {}".format(exc))
    else:
        rospy.loginfo("The response from server is \"{}\"".format(respone_from_server))

def parse_arguments():
    parser = argparse.ArgumentParser(description="Provide 2 integers to be added")
    parser.add_argument("-i", "--integers", type=int, nargs=2, help="The first integer", required=True)
    return parser.parse_args()

if __name__=="__main__":
    args = parse_arguments()
    main(args.integers[0], args.integers[1])

