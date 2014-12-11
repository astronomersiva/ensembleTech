#!/usr/bin/python

import serial
import time
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)

while True:
	s = serial.Serial('/dev/ttyAMA0')
	temp = int(s.readline().strip('\n')) / 2
	print temp
	if temp > 30:
		GPIO.output(4, True)
		break

time.sleep(2)
GPIO.output(4, False)


