#!/usr/bin/pythonRoot
import RPi.GPIO as GPIO     
from flup.server.fcgi import WSGIServer 
import sys
import urlparse

# set up our GPIO pins
GPIO.setmode(G.BOARD)
GPIO.setup(7, GPIO.OUT) #use any GPIO pin
GPIO.setup(3, GPIO.OUT) #use any GPIO pin


def app(environ, start_response): 
  start_response("200 OK", [("Content-Type", "text/html")])
  i = urlparse.parse_qs(environ["QUERY_STRING"])
  yield ('&nbsp;')
  if "led" in i:
    if i["led"][0] == "led1On": 
      GPIO.output(7, True)   # Turn it on
    elif i["led"][0] == "led1Off":
      GPIO.output(7, False)  # Turn it off
	elif i["led"][0] == "led2On":
      GPIO.output(3, True)  # Turn it off
	elif i["led"][0] == "led2Offf":
      GPIO.output(3, False)  # Turn it off


WSGIServer(app).run()
