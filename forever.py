#!/usr/bin/python
from subprocess import Popen

while True:
    print("\nStarting BOT ")
    p = Popen("python index.py", shell=True)
    p.wait() 