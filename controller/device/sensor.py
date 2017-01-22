from controller.device.end_device import EndDevice
import rospy
from std_msgs.msg import String, Float32

class Sensor(EndDevice):
    def __init__(self, cid, did, Type, tid, address, topic):
        super(Sensor, self).__init__(cid, did, Type, tid, address)
        self.topic = topic
        self.value = None

    def callback(self, data):
        print(data.data)
        rospy.signal_shutdown('once')
        return data.data

    def get_value(self):
        rospy.init_node(self.TYPE, anonymous=True, disable_signals=True)
        rospy.Subscriber(self.topic, String, self.callback)
        a=rospy.spin()
        print(a)
