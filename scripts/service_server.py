#!/usr/bin/env python3
import rospy

from ros_fundamentals.srv import AddTwoIntegers, AddTwoIntegersResponse


def main():
    # name of service, type of service and callback
    server = rospy.Service(name="addition_service", service_class=AddTwoIntegers, handler=callback)
    rospy.init_node(name="addition_server")

    rospy.spin()


def callback(request):
    # return request.AddTwoIntegersResponse(request.a + request.b)
    return request.a + request.b


if __name__ == "__main__":
    main()
