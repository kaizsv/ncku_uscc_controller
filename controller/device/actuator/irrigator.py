from controller.device.actuator.actuator import Actuator

class IrrActuator(Actuator):
    def __init__(self, cid, did, Type, tid, address):
        super(IrrActuator, self).__init__(cid, did, Type, tid, address)

    '''def make_action(self, action):
        print('actuator {0} take an action {1}'.format(self.TID, action))
    '''
