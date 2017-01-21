from controller.device.actuator.actuator import Actuator

class MotorActuator(Actuator):
    def __init__(self, cid, did, Type, tid, address):
        super(MotorActuator, self).__init__(cid, did, Type, tid, address)
