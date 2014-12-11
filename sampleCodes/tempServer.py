#!/usr/bin/python

import web
import serial
import time


urls = ('/', 'index')

class index:
    def GET(self):
        s = serial.Serial('/dev/ttyAMA0')
	temp = int(s.readline().strip('\n')) / 2
        return str(temp)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
