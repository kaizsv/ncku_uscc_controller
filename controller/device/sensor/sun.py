from controller.device.sensor.sensor import Sensor

class Sun(Sensor):
    def __init__(self, cid, did, Type, tid, address):
        super(Sun, self).__init__(cid, did, Type, tid, address)
