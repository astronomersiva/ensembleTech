#!/usr/bin/python

import web
import serial
import time


urls = ('/', 'index')

class index:
    def GET(self):
        s = serial.Serial('/dev/ttyAMA0')
	ldr = str(s.readline().strip('\n'))
        return ldr

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
