#!/usr/bin/python
from raspirgb import RaspiRGB
import SimpleHTTPServer
import SocketServer
import re

PORT = 8000

rgb = RaspiRGB()

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			resp = open('server.html', 'r').read()
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.send_header("Content-length", len(resp))
			self.end_headers()
			self.wfile.write(resp)
		elif self.path.startswith('/set-'):
			self.send_response(200)
			s = self.path[-6:]
			r, g, b = int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)
			rgb.set(r, g, b)
		else:
			self.send_response(404)

httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
