import rospy
from std_msgs.msg import String, Int32

#rostopic echo /relay1
'''
def cb_once(msg):
    print('gg')
    print(msg.data)
    rospy.signal_shutdown('g')

rospy.init_node('listener', anonymous=True, disable_signals=True)
rospy.Subscriber('relay1', String, cb_once)
rospy.spin()

'''
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('relay1', Int32, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

