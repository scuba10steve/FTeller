import logging

class Logger(object):
    """docstring for Logger"""
    def __init__(self):
        super(Logger, self).__init__()
	try:
	    import http.client as http_client
	except ImportError:
	    # Python 2
	    import httplib as http_client
	http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
	logging.getLogger().setLevel(logging.DEBUG)

    def warn()
