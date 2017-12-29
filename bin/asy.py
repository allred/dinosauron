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
    r = d.dig_async(targets)

if __name__ == "__main__":
    target = "localhost"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    scan([target])
