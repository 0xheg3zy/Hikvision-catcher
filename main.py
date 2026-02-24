import socket
import struct
import uuid
import xml.etree.ElementTree as ET
import time

MCAST_GRP = "239.255.255.250"
PORT = 37020

# Build probe XML with random UUID
probe_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<Probe>
    <Uuid>{uuid.uuid4()}</Uuid>
    <Types>inquiry</Types>
</Probe>'''.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.settimeout(5)

sock.sendto(probe_xml, (MCAST_GRP, PORT))

print("Searching for Hikvision devices...\n")

start = time.time()

while time.time() - start < 5:
    try:
        data, addr = sock.recvfrom(8192)
        try:
            xml_data = data.decode(errors="ignore")
#            print("data is : \n"+xml_data)
            root = ET.fromstring(xml_data)

            model = root.findtext("DeviceDescription")
            serial = root.findtext("DeviceSN")
            firmware = root.findtext("SoftwareVersion")
            dsp = root.findtext("DSPVersion")
            ip = root.findtext("IPv4Address")

            print("Found device:")
            print(f"  IP: {ip}")
            print(f"  Model: {model}")
            print(f"  Serial: {serial}")
            print(f"  Firmware: {firmware}")
            print(f"  DSP: {dsp}")
            print("-" * 40)

        except ET.ParseError:
            continue

    except socket.timeout:
        break

sock.close()
