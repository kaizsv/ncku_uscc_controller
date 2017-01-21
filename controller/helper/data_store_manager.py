from controller.helper.log import Log
from controller.device.rule import Rule

class DataStoreManager(object):

    dac_threads = dict()

    def __init__(self):
        pass

    def append_dac_thread(self, did, dac_thread):
        DataStoreManager.dac_threads[did] = dac_thread

    def get_dac_thread_by_id(self, did):
        return DataStoreManager.dac_threads[did]

    def assign_end_device_to_dac(self, did, end_device):
        dac_thread = self.get_dac_thread_by_id(did)
        dac_thread.assign_end_device(end_device)

    @staticmethod
    def assign_schedule_to_dac(rpc_schedule):
        rules = list()
        for rule in rpc_schedule:
            r = Rule(rule)
            if not r.initialize(rule):
                return False
            rules.append(r)
        for rule in rules:
            for target_tid in rule.target_tid:
                thread = DataStoreManager.dac_threads[target_tid]
                thread.assign_rule_to_dac_schedule(rule)
        return True
