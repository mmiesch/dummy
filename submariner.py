"""
The purpose of this code is to test the integration of another repo through git submodule
"""

import sys
sys.path.insert(0,'./CIMP')

from CIMP import Event as ev

print("Starting our submarine adventure")

x = ev.event.testcase(1)

