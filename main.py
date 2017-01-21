from controller.helper.log import Log
from controller.helper.data_store_manager import DataStoreManager
from controller.dac.DAC_controller import DACController
from controller.comm.rpc import run_rpc_server
from controller.comm.ros_device_subscriber import RosDeviceSubscriber
from controller.device.actuator.irrigator import IrrActuator
from controller.device.sensor.humidity import HumidSensor
import os
import rospy

def callback(data):
    print(data.data)
    rospy.signal_shutdown('s')

def listener():
    rospy.init_node('listener', anonymous=True, disable_signals=True)
    rospy.Subscriber('hello', String, callback)
    rospy.spin()

def main():
    log = Log(Log.DEBUG, __file__)

    cid = get_controller_ip()
    log.info('controller ip: {0}'.format(cid))

    data_store_manager = DataStoreManager()

    log.info('start rpc server')
    run_rpc_server()

    #ros_device_subscriber = RosDeviceSubscriber()
    #ros_device_subscriber.start()

    #listener()

    #while
    did = 0
    log.info('start a new dac thread, did: {0}'.format(did))
    thread = DACController(data_store_manager, cid, did)
    thread.initial()

    tid = 0
    log.info('new irrigrate actuator at did: {0}, type:{1}, tid:{2}'.format(did, 'AW', tid))
    irr = IrrActuator(cid, did, 'AW', tid, 40000)
    data_store_manager.assign_end_device_to_dac(did, irr)

    tid = 1
    log.info('new humid sensor at did: {0}, type:{1}, tid:{2}'.format(did, 'S', tid))
    humid = HumidSensor(cid, did, 'S', tid, 40001)
    data_store_manager.assign_end_device_to_dac(did, humid)

    did = 1
    log.info('start a new dac thread, did: {0}'.format(did))
    thread = DACController(data_store_manager, cid, did)
    thread.initial()

def get_controller_ip():
    f = os.popen('ifconfig | grep "inet\ addr" | grep -v "127.0.0.1" | cut -d: -f 2 | cut -d" " -f 1 | tr -d "\n"')
    ip = f.read()
    if ip == '':
        ip = '127.0.0.1'
    return ip

if __name__ == "__main__":
    main()
