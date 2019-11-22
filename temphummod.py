def readtemphumid():

	import mysql.connector
	import RPi.GPIO
	import Adafruit_DHT
	sensor=Adafruit_DHT.DHT11
	import os
	import glob
	import time
	os.system('modprobe w1-gpio')  # Turns on the GPIO module
	os.system('modprobe w1-therm') # Turns on the Temperature module
	gpio=17

	# Finds the correct device file that holds the temperature data
	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28*')[0]
	device_file = device_folder + '/w1_slave'

	# A function that reads the sensors data
	def read_temp_raw():
		f = open(device_file, 'r') # Opens the temperature device file
		lines = f.readlines() # Returns the text
		f.close()
		return lines
		
	# Convert the value of the sensor into a temperature
	def read_temp():
		lines = read_temp_raw() # Read the temperature 'device file'
	 
		# While the first line does not contain 'YES', wait for 0.2s
		# and then read the device file again.
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = read_temp_raw()
	 
		# Look for the position of the '=' in the second line of the
		# device file.
		equals_pos = lines[1].find('t=')
	 
		# If the '=' is found, convert the rest of the line after the
		# '=' into degrees Celsius, then degrees Fahrenheit
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			return temp_c

	while abs((temp_dht11-read_temp())) > 0.5:
		if humidity is None and temperature is None:
			print('Failed to get temperature/humidity reading. Possible hardware problem!')
			break
		humid_dht11, temp_dht11 = Adafruit_DHT.read_retry(sensor, gpio)
		
	humid=humid_dht11
	temp=temp_dht11

	#-----------------------------------------------------------------------------------------------------#


	#connecting the database
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="yourusername",
	  passwd="yourpassword"
	)

	mycursor = mydb.cursor()

	#database structure of temp and humid
	#mycursor.execute("CREATE TABLE temp_humid(id INT(4), time1 DATETIME, temp INT(4), humid INT(4))")

	import datetime
	current_datetime = datetime.datetime.now().strftime("%c")


	sql = "INSERT INTO temp_humid(datetime1, temp, humid, sensor_id) VALUES (%s, %s, %s)"
	val = (current_datetime, temp, humid, 001)
	mycursor.execute(sql, val)

	mydb.commit()
