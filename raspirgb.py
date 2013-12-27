import smbus

class RaspiRGB(object):

	ADDR  = 0x61
	PWM_R = 13
	PWM_G = 14
	PWM_B = 15

	def __init__(self):
		self.bus = smbus.SMBus(1)
		self.bus.write_byte_data(self.ADDR, 0x00, 0x00)
		self.bus.write_byte_data(self.ADDR, 0x14, 0xAA)
		self.bus.write_byte_data(self.ADDR, 0x15, 0xAA)
		self.bus.write_byte_data(self.ADDR, 0x16, 0xAA)
		self.bus.write_byte_data(self.ADDR, 0x17, 0xAA)
		self.set(0, 0, 0)

	def set(self, r, g, b):
		self.setr(r)
		self.setg(g)
		self.setb(b)

	def setr(self, v):
		self.bus.write_byte_data(self.ADDR, 2 + self.PWM_R, int(v))

	def setg(self, v):
		self.bus.write_byte_data(self.ADDR, 2 + self.PWM_G, int(v))

	def setb(self, v):
		self.bus.write_byte_data(self.ADDR, 2 + self.PWM_B, int(v))
