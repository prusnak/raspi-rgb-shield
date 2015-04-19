#!/usr/bin/python
from raspirgb import RaspiRGB
import math
import time

rgb = RaspiRGB()

t = 0.0

while True:
	r = 128 + 127 * math.sin(1.0 * t)
	g = 128 + 127 * math.sin(1.5 * t)
	b = 128 + 127 * math.sin(2.0 * t)
	rgb.setrgb(r, g, b)
	t += 0.01
	time.sleep(0.01)
