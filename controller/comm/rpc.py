from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from controller.helper.data_store_manager import DataStoreManager
import threading

class ReuqestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def rpc_set_rule(rpc_schedule):
    if DataStoreManager.assign_schedule_to_dac(rpc_schedule):
        return 'SUCCESS'
    else:
        return 'FAILURE'

def rpc_set_imm_rule(rpc_rule):
    if DataStoreManager.assign_schedule_to_dac(rpc_rule):
        return 'SUCCESS'
    else:
        return 'FAILURE'

def rpc_server():
    server = SimpleXMLRPCServer(("localhost", 8000),
                                requestHandler=ReuqestHandler)
    server.register_introspection_functions()

    server.register_function(rpc_set_rule, 'rpc_set_rule')

    server.register_function(rpc_set_imm_rule, 'rpc_set_imm_rule')

    server.serve_forever()

def run_rpc_server():
    threading.Thread(target=rpc_server).start()
