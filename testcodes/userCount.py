import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor


global user_counter
user_counter = 0

while True:
	i=GPIO.input(12)
if i==0:                 #When output from motion sensor is LOW
	print "No intruders",i

	time.sleep(0.1)

elif i==1:               #When output from motion sensor is HIGH
	print "Intruder detected",i

	user_counter+=1
	time.sleep(0.1)