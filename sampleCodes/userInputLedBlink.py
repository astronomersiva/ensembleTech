import RPi.GPIO as GPIO
import time

#turns on and blinks an LED for a number of times
#specified by the user.

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)

try:
    noOfTimes = int(raw_input("Enter the number of blinks"))
except:
    print 'Please enter an integer value'

try:
    blinkDuration = float(raw_input("Enter the duration of the blinks"))
except:
    print 'Please enter a number'

for n in xrange(noOfTimes):    
    GPIO.output(7, True)
    time.sleep(blinkDuration)
    GPIO.output(7, False)
    time.sleep(blinkDuration)s
