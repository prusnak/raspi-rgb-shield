import time

class RaspiRGB(object):

	ADDR  = 0x61
	PWM_RED = 13
	PWM_GREEN = 14
	PWM_BLUE = 15

	def __init__(self):
		try:
			import smbus
			self.bus = smbus.SMBus(1)
			print 'I2C bus found: %s' % self.bus
		except:
			print 'I2C bus NOT found'
			self.bus = None
		self.write(0x00, 0x01)
		self.write(0x01, 0x00)
		self.write(0x14, 0xAA)
		self.write(0x15, 0xAA)
		self.write(0x16, 0xAA)
		self.write(0x17, 0xAA)
		self.setrgb(0, 0, 0)

	def write(self, channel, data):
		if self.bus:
			self.bus.write_byte_data(self.ADDR, channel & 0xFF, data & 0xFF)
			time.sleep(0.001)

	def setrgb(self, r, g, b):
		self.setr(r)
		self.setg(g)
		self.setb(b)

	def setraw(self, i, v):
		self.write(2 + int(i), int(v))

	def setr(self, v):
		self.write(2 + self.PWM_RED, int(v))

	def setg(self, v):
		self.write(2 + self.PWM_GREEN, int(v))

	def setb(self, v):
		self.write(2 + self.PWM_BLUE, int(v))
