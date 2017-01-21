from controller.device.sensor.sensor import Sensor

class AirTemperature(Sensor):
    def __init__(self, cid, did, Type, tid, address):
        super(AirTemperature, self).__init__(cid, did, Type, tid, address)
