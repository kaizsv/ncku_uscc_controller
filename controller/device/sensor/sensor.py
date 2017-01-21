from controller.device.end_device import EndDevice

class Sensor(EndDevice):
    def __init__(self, cid, did, Type, tid, address):
        super(Sensor, self).__init__(cid, did, Type, tid, address)

    def get_value(self):
        return 41
