import random
import string

import cherrypy

from posttroll.publisher import Publish
from posttroll.message import Message

import time

class StringGenerator(object):
    def __init__(self):
	self.publisher=Publish("webtroll",9000)

    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="Test message" name="message" />
              <button type="submit">Send Posttroll message</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, message="Test message"):
	
	with self.publisher as pub:
		time.sleep(1)
		msg=Message("/www/interface","info",message)
		pub.send(str(msg))
	
        return "Sent message: "+message+"""
	<br/><br/>
	<a href="/">Go back</a>
	"""

if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(StringGenerator())
