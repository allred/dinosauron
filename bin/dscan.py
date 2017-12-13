#!/usr/bin/env python
import datetime
import json
import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))
from dinosauron import dinosauron
from dinosauron import dino_nmap

def scan(targets):
    t_start = int(time.time())
    d = dinosauron.Dinosauron()
    dn = dino_nmap.DinoNmap()
    report = dn.do_scan(targets, "-Pn -T5 -F")
    for host in report.hosts:
        mdns_out = d.dig_mdns(host.address)
        if mdns_out or len(host.get_ports()) > 0:
            d = host.get_dict()
            hostnames = d.get("hostnames", "")
            hostname = hostnames.split(' ')[0]
            if hostname == '' and mdns_out:
                hostname = mdns_out.strip().decode('ascii')
            output = f'{host.address:<13} {hostname} {host.get_ports()}'
            print(output)
    t_end = int(time.time())
    s_elapsed = t_end - t_start
    footer = f'{s_elapsed}s'
    print(footer)

if __name__ == "__main__":
    target = "localhost"
    if len(sys.argv) > 1:
        target = sys.argv[1]
        scan([target])
