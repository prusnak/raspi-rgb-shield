#!/usr/bin/python
import tornado.ioloop
import tornado.web
from raspirgb import RaspiRGB
from myip import get_my_ip

PORT = 8000

rgb = RaspiRGB()

def get_my_ip():
	try:
		import netifaces
		for iface in [ x for x in netifaces.interfaces() if x != 'lo' ]:
			try:
				return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
			except:
				pass
		return '127.0.0.1'
	except:
		return '127.0.0.1'

class HandlerPage(tornado.web.RequestHandler):
	def get(self):
		resp = open('test-server.html', 'r').read()
		self.write(resp)

class HandlerSetColor(tornado.web.RequestHandler):
	def get(self):
		s = self.request.uri[-6:]
		r, g, b = int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)
		rgb.set(r, g, b)
		self.write("OK")

application = tornado.web.Application([
	(r"/", HandlerPage),
	(r"/set/.*", HandlerSetColor),
])

def main():
	print 'Starting server at %s:%d ...' % (get_my_ip(), PORT)
	application.listen(PORT)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
