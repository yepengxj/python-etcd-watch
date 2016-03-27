import etcd
import time

client = etcd.Client(port=2379)

c = 0
for event in client.eternal_watch('/nodes',recursive=True):
    #print event.key , event.value
    print event
    c += 1
    print c
    time.sleep(1)
