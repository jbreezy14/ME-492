# Jabril Cross-Ellis
# MRE 492
# Homework 3 - 4 

import RPi.GPIO as GPIO
import time 

try: 
	GPIO.setmode(GPIO.BCM)

	TRIG = 4
	ECHO = 17

	print "calculating Distance"

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG,GPIO.LOW)
	print "allowing sensor to steady"
	time.sleep(2)

	GPIO.output(TRIG, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(TRIG, GPIO.LOW)

	while GPIO.input(ECHO) ==0:
		pulse_start = time.time()

	while GPIO.input(ECHO) ==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration*17150
	distance = round(distance, 2)

	print "Distance:",distance,"cm"

finally:
	GPIO.cleanup()
