#!/usr/bin/env python3.5
from subprocess import Popen
import sys

filename = sys.argv[1]
while True:
    print("\nStarting " + filename)
    p = Popen("python3.5 " + filename, shell=True)
    p.wait()
    
# https://www.alexkras.com/how-to-restart-python-script-after-exception-and-run-it-forever/
# Next, I can start my program with:
# ./forever test.py
# nohup ./forever main.py &
