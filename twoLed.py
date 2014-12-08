import RPi.GPIO as GPIO
import time

#turns on an LED
#waits for two seconds
#and switches it off
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.output(7, True)
time.sleep(2)
GPIO.output(7, False)
GPIO.output(3, True)
time.sleep(2)
GPIO.output(3, False)
