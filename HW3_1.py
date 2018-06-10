#Jabril Cross-Ellis
#ME 492
#Hw 3-1

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = [4,17,18,27]

for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)
	for j in range(1):
		GPIO.output(pin,1)
		time.sleep(1.0)
		GPIO.output(pin,0)
		time.sleep(0.1)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
pins = [27,18,17,4]

for i, pin in enumerate(pins):
	GPIO.setup(pin,GPIO.OUT)
	for j in range(1):
		GPIO.output(pin,1)
		time.sleep(1.0)
		GPIO.output(pin,0)
		time.sleep(0.5)
GPIO.cleanup()
