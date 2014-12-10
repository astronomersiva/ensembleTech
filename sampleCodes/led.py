#!/usr/bin/pythonRoot

import RPi.GPIO as GPIO     
from flup.server.fcgi import WSGIServer 
import sys
import urlparse

# set up our GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) #use any GPIO pin
GPIO.setup(2, GPIO.OUT)


def app(environ, start_response): 
  start_response("200 OK", [("Content-Type", "text/html")])
  i = urlparse.parse_qs(environ["QUERY_STRING"])
  yield ('&nbsp;')
  if "status" in i:
	if i["status"][0] == "1on":
		GPIO.output(4,True)
	if i["status"][0] == "1off":
		GPIO.output(4,False)
	if i["status"][0] == "2on":
		GPIO.output(2,True)
	if i["status"][0] == "2off":
		GPIO.output(2,False)
		

WSGIServer(app).run()
