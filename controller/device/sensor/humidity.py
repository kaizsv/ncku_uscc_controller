from controller.device.sensor.sensor import Sensor

class HumidSensor(Sensor):
    def __init__(self, cid, did, Type, tid, address):
        super(HumidSensor, self).__init__(cid, did, Type, tid, address)
