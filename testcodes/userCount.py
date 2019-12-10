import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)         #Read output from PIR motion sensor


global user_counter
user_counter = 0

print "Start sequence"
print user_counter


while True:
	i=GPIO.input(18)
if i==0:                 #When output from motion sensor is LOW
	print "No intruders",i
	print user_counter
	time.sleep(0.5)

elif i==1:               #When output from motion sensor is HIGH
	print "Intruder detected",i
	user_counter+=1
	print user_counter
	time.sleep(0.5)
