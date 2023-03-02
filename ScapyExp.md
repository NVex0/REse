#Netlab2
```
from scapy.all import *
import base64
import base58

pcap = rdpcap(r"D:\temporary\netlab2.pcap")
def cleanse(strings):
    if '.' in strings:
        return strings.replace('.', '')
    return strings

out = ""
for pkt in pcap:
    if pkt.haslayer(DNSQR):
        strings = str(pkt[DNSQR].qname)[2:-2]
        if not 'local' in strings:
            tmp = strings.split("-")
            specify = base58.b58decode(cleanse(tmp[-1]))
            if specify == b'Flag.kdbx\n':
                tmp.pop(-1)
                for i in tmp:
                    out += cleanse(i)
out = out.replace('{', '/')
out = out.replace('}', '+')
fin = base64.b64decode(out)
with open ("Flag.zip", "wb") as f:
    f.write(bytearray(fin))
```
