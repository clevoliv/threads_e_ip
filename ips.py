import ipaddress

ip = '192.168.0.1'
net = '192.168.0.0/24'

adr = ipaddress.ip_address(ip)
adr_net = ipaddress.ip_network(net, strict=False)
print(adr + 100)
for net in adr_net:
    # increment ip address
    print(net)
