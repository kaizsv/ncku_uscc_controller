from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib, threading, os, time


global server_ip
server_ip_port = "http://192.168.1.15:8000"
server_ip = "192.168.1.15"

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def rpc_send_data(immediate_control):
    # connection to rpc server
    server = xmlrpclib.ServerProxy((server_ip_port), allow_none=True)
    print(server.rpc_set_rule(immediate_control))

def rpc_get_sensor_data(tid):
    server = xmlrpclib.ServerProxy((server_ip_port), allow_none=True)
    return server.rpc_get_sensor_value(tid)
