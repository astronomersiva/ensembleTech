import urllib2
import time
import matplotlib.pyplot as plt

t = []
lightValues = []

print 'please wait..values are being read'

for x in range(1, 10):
    t.append(x)
    ldr = int(urllib2.urlopen('http://192.168.0.32:8080').read())
    lightValues.append(ldr)
    time.sleep(2)

plt.plot(t, lightValues)
plt.show()
