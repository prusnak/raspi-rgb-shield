#!/usr/bin/python
from raspirgb import RaspiRGB

rgb = RaspiRGB()

while True:
    r = 128 + 127 * math.sin(1.0 * t)
    g = 128 + 127 * math.sin(1.5 * t)
    b = 128 + 127 * math.sin(2.0 * t)
    rgb.set(r, g, b)
    t += 0.1
    time.sleep(0.01)
