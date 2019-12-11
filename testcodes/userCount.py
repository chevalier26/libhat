import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)         #Read output from PIR motion sensor


global user_counter
global delayChecker

delayChecker = 0
user_counter = 0

print "Start sequence"
print user_counter

while True:
	i=GPIO.input(18)
if i==0:                 #When output from motion sensor is LOW
	print "No intruders, (",i, ")"
	print user_counter
	time.sleep(1)
	delayChecker = 0

else if i==1:               #When output from motion sensor is HIGH
	print "Intruder detected, (", i, ")"
	user_counter+=1
	print "People: ", user_counter#, "\n"
	print "[Delay: ", delayChecker, "]", "\n"
	time.sleep(1)
