# python-etcd-watch
import etcd
client = etcd.Client(port=2379)
c = 0
for i in range(100):
   client.write('/nodes/n%s'%i, 1,ttl=10)
   c += 1
   print i

for i in range(100):
   client.delete('/nodes/n%s'%i, 1)
   c += 1
   print i

for i in range(100):
   client.write('/nodes/n%s'%i, 1,ttl=10)
   c += 1
   print i
