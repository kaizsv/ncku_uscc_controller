from controller.device.end_device import EndDevice
from threading import Timer
import time

class Actuator(EndDevice):
    def __init__(self, cid, did, Type, tid, address, pub):
        super(Actuator, self).__init__(cid, did, Type, tid, address)
        self.curr_setting = 0
        self.publisher = pub

    def make_action(self, action):
        self.publisher.publish(action)
        print('actuator {0} take an action {1}'.format(self.TID, action))
        self.curr_setting = action

    def schedule_action(self, action, duration):
        pre_action = self.curr_setting
        self.make_action(action)
        self.timer = Timer(duration, self.make_action, (pre_action,)).start()

    def stop_schedule_action(self):
        if self.timer:
            self.timer.cancel()
