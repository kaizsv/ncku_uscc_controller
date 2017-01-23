import rospy
from std_msgs.msg import String, Int32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('relay4', Int32, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
