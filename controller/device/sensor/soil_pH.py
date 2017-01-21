from controller.device.sensor.sensor import Sensor

class SoilpH(Sensor):
    def __init__(self, cid, did, Type, tid, address):
        super(SoilpH, self).__init__(cid, did, Type, tid, address)
