import rospy
import threading
from std_msgs.msg import Float32, Int32, String

def callback(data):
    with open('../../all_devices.txt', 'w') as f:
        f.write(data.data)

class RosDeviceSubscriber(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber('name', String, callback)

        rospy.spin()
'''
if __name__ == '__main__':
    listener()
'''
