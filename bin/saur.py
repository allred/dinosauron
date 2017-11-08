#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))
from dinosauron import cli

c = cli.Chui()
c.run()
