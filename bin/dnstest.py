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
    d = dinosauron.Dinosauron()
    dn = dino_nmap.DinoNmap()
    res = dns.resolver.Resolver()
    #res.nameservers = ["8.8.8.8"]
    #b = res.query("yahoo.com", "A")
    #print(b[0])
    res.nameservers = ["224.0.0.251"]
    res.port = 5353
    #res.timeout = 1
    #res.lifetime = 1
    a = res.query("113-0-168-192.in-addr.arpa", "PTR")

if __name__ == "__main__":
    target = "localhost"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    scan([target])
