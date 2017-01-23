import xmlrpclib as rpc

conn = rpc.ServerProxy("http://192.168.1.30:8080")

print conn.echo('test')

print conn.register('controller', {'CID':'192.168.1.30'})
print conn.register('dac', {'CID':'192.168.1.30','DID':'2'})
print conn.register('sensor', {'CID':'192.168.1.30','DID':'1','Type':'B','Address':'40030'})
print conn.register('actuator', {'CID':'192.168.1.30','DID':'1','Type':'B','Address':'40005'})

print conn.event('disconnect','controller',{'CID':'192.168.1.30'})
