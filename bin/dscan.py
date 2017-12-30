#!/usr/bin/env python
import datetime
import dns.resolver
import json
import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))
from dinosauron import dinosauron
from dinosauron import dino_nmap


def scan(targets):
    t_start = int(time.time())
    dn = dino_nmap.DinoNmap()
    d = dinosauron.Dinosauron()
    host_list = dn.scan_list(targets)
    args_nmap = "-Pn -T5 -F"
    report = dn.do_scan(targets, args_nmap)
    for host in report.hosts:
        mdns_out = d.query_mdns(host.address)
        if mdns_out or len(host.get_ports()) > 0:
            host_dict = host.get_dict()
            hostnames = host_dict.get("hostnames", "")
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
