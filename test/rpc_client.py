import xmlrpclib
import time
import os

def getip():
    f = os.popen('ifconfig | grep "inet\ addr" | grep -v "127.0.0.1" | cut -d: -f 2 | cut -d" " -f 1 | tr -d "\n"').read()
    if f == '':
        f = '127.0.0.1'
    return f

cid = getip()

schedule = [
    {
        'condition':[{'sensor':{'CID':cid,'DID':0,'TYPE':'S','TID':1,'ADDRESS':40001},'operator':1,'threshold':40}],
        'action':[{'actuator':{'CID':cid, 'DID':0, 'TYPE':'AW', 'TID':0, 'ADDRESS':40000}, 'value':1}],
        'period':{'start_time':14, 'duration':0},
        'rule_make_time':time.strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        'condition':[],
        'action':[{'actuator':{'CID':cid, 'DID':0, 'TYPE':'AW', 'TID':0, 'ADDRESS':40000}, 'value':1}],
        'period':{'start_time':'2017-01-21 03:08:00', 'duration':0},
        'rule_make_time':time.strftime("%Y-%m-%d %H:%M:%S")
    }
]

s = xmlrpclib.ServerProxy('http://localhost:8000')
print(s.rpc_set_rule(schedule))
