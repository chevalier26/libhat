import RPi.GPIO as GPIO
import time
import mysql.connector

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)         #Read output from PIR motion sensor


global user_counter
global delayChecker

delayChecker = 0
user_counter = 0

	#connecting the database
mydb = mysql.connector.connect(
	 host="localhost",
	 user="pi",
	 passwd="raspberry",
	 database="libhat"
)

print "Database Connected"
mycursor = mydb.cursor()

import datetime

print "START SEQUENCE"
time.sleep(3)


while True:
	i=GPIO.input(18)
	if i==0:                 #When output from motion sensor is LOW
		print "No intruders, (",i,")"
		print "People: ", user_counter, "\n"
		time.sleep(1)
		delayChecker = 0

	elif i==1:               #When output from motion sensor is HIGH
		print "Intruder detected, (",i,")"
		user_counter+=1
		print "People: ", user_counter, "\n"
		time.sleep(2)
		while i==1:
			i=GPIO.input(18)
			delayChecker+=1
			print "[Delay:", delayChecker,"]", i,"\n"
			time.sleep(1)

	current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	sql = "INSERT INTO user_count(datetime1, user_count, sensor_id) VALUES (%s,%s,%s)"
	sensor_id=001
	val = (current_datetime, user_counter, sensor_id)
	mycursor.execute(sql, val)

	mydb.commit()

	print "Data transferred"
