from controller.device.sensor.sensor import Sensor

class AirHumidity(Sensor):
    def __init__(self, cid, did, Type, tid, address):
        super(AirHumidity, self).__init__(cid, did, Type, tid, address)
