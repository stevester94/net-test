#! /usr/bin/env python3
import sys
import re
import matplotlib.pyplot as plt

with open(sys.argv[1], "r") as f:
    lines = f.read()

r = r"\[(.*)\].*time=(.*) ms"
times = []
stamps = []
for line in lines.split("\n"):
    res = re.findall( r, line )
    if len(res) == 0:continue
    elif len(res) == 1: res = res[0]
    else: raise Exception( f"Got a weird line: {line}" )

    stamp = float(res[0])
    time  = float(res[1])

    times.append(time)
    stamps.append(stamps)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20,20))

histAx = ax[0][0]
temporalAx = ax[0][1]


histAx.hist(times, bins=10)

temporalAx.plot( times )

plt.show()