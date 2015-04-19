class RaspiRGB(object):

	ADDR  = 0x61
	PWM_R = 13
	PWM_G = 14
	PWM_B = 15

	def __init__(self):
		try:
			import smbus
			self.bus = smbus.SMBus(1)
			print 'I2C bus found: %s' % self.bus
		except:
			print 'I2C bus NOT found'
			self.bus = None
		if self.bus:
			self.bus.write_byte_data(self.ADDR, 0x00, 0x00)
			self.bus.write_byte_data(self.ADDR, 0x14, 0xAA)
			self.bus.write_byte_data(self.ADDR, 0x15, 0xAA)
			self.bus.write_byte_data(self.ADDR, 0x16, 0xAA)
			self.bus.write_byte_data(self.ADDR, 0x17, 0xAA)
			self.setrgb(0, 0, 0)

	def setrgb(self, r, g, b):
		self.setr(r)
		self.setg(g)
		self.setb(b)

	def setraw(self, i, v):
		if self.bus:
			self.bus.write_byte_data(self.ADDR, 2 + int(i), int(v))

	def setr(self, v):
		if self.bus:
			self.bus.write_byte_data(self.ADDR, 2 + self.PWM_R, int(v))

	def setg(self, v):
		if self.bus:
			self.bus.write_byte_data(self.ADDR, 2 + self.PWM_G, int(v))

	def setb(self, v):
		if self.bus:
			self.bus.write_byte_data(self.ADDR, 2 + self.PWM_B, int(v))
