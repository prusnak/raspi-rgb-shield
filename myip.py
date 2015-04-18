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
