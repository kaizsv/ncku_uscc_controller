from controller.device.sensor.sensor import Sensor

class SoilHumiditiy(Sensor):
    def __init__(self, cid, did, Type, tid, address):
        super(SoilHumiditiy, self).__init__(cid, did, Type, tid, address)
