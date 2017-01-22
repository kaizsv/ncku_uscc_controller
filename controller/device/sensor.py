from controller.device.end_device import EndDevice
import rospy
from std_msgs.msg import String, Float32

class Sensor(EndDevice):
    def __init__(self, cid, did, Type, tid, address, topic):
        super(Sensor, self).__init__(cid, did, Type, tid, address)
        self.topic = topic
        self.value = None

    def callback(self, data):
        self.value = data.data

    def subscribe_value(self):
        rospy.Subscriber(self.topic, String, self.callback)

    def get_value(self):
        return self.value
