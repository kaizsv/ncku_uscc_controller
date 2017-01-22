from controller.device.end_device import EndDevice
from threading import Timer
import time
import rospy
from std_msgs.msg import String, Int32

class Actuator(EndDevice):
    def __init__(self, cid, did, Type, tid, address, send_queue):
        super(Actuator, self).__init__(cid, did, Type, tid, address)
        self.curr_setting = 0
        self.send_queue = send_queue

    def make_action(self, action):
        self.send_queue.put('actuator {0} take an action{1}'.format(self.TID, action))
        print('actuator {0} take an action {1}'.format(self.TID, action))
        self.curr_setting = action
        '''
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('actuator', anonymous=True)
        rate = rospy.Rate(10)
        send_data = 'actuator {0} take an action {1}'.format(self.TID, action)
        pub.publish(send_data)
        rate.sleep()
        '''

    def schedule_action(self, action, duration):
        pre_action = self.curr_setting
        self.make_action(action)
        self.timer = Timer(duration, self.make_action, (pre_action,)).start()

    def stop_schedule_action(self):
        if self.timer:
            self.timer.cancel()
