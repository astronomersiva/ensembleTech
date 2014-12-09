import gmail
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)

print 'authenticating. please wait'

g = gmail.login('username', 'password')
while True:
	commandMails = g.inbox().mail(unread = True, sender = 'sourceEmailgmail.com', subject = 'LED')
	try:	
		commandMails[0].fetch()
		command = commandMails[0].body.lower()
		commandMails[0].delete()
		if 'light' in command or 'lite' in command:
			if 'on' in command:
				GPIO.output(7, True)
			if 'off' in command or 'of' in command:
				GPIO.output(7, False)
		else:
			pass
	except:
		time.sleep(10)
