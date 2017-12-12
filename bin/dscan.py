#!/usr/bin/env python
import json
import os
import sys
import subprocess
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))
from dinosauron import dino_nmap

def query_mdns(address):
    proc = subprocess.Popen(["dig", "+time=1", "+short", "-x", address, "@224.0.0.251", "-p", "5353"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    if proc.returncode == 0:
        return out
    else:
        return None

def scan(targets):
    report = dino_nmap.do_scan(targets, "-Pn -T5 -F")
    for host in report.hosts:
        if len(host.get_ports()) > 0:
            d = host.get_dict()
            hostnames = d.get("hostnames", "")
            hostname = hostnames.split(' ')[0]
            if hostname == '':
                mdns_out = query_mdns(host.address)
                if mdns_out:
                    hostname = mdns_out.strip().decode('ascii')
            output = f'{host.address:<13} {hostname} {host.get_ports()}'
            print(output)
    footer = f'{report.elapsed}s'
    print(footer)

target = "localhost"
if len(sys.argv) > 1:
   target = sys.argv[1]
scan([target])
