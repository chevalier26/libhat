def read_sound():
    # Import SPI library (for hardware SPI) and MCP3008 library.
    import Adafruit_GPIO.SPI as SPI
    import Adafruit_MCP3008
    import mysql.connector
    import RPi.GPIO as GPIO
    import os
    import glob
    import time
    import datetime
 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.OUT)
	
    # Software SPI configuration:
    # CLK  = 18
    # MISO = 23
    # MOSI = 24
    # CS   = 25
    # mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    # Hardware SPI configuration:
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

    #connecting the database
    mydb = mysql.connector.connect(
    	 host="localhost",
    	 user="pi",
    	 passwd="raspberry",
    	 database="libhat"
	)
    print "connected"
    mycursor = mydb.cursor()

    #sound database
    #mycursor.execute("CREATE TABLE sound_sensor(id INT(4), datetime1 DATETIME, sound_level INT(4), sensor_id)")
    x = 0
    #calibrating
    print "Calibrating ambient noise. Wait 5 seconds"
    while x != 5:
        x += 1
        time.sleep(1)
    ambientSound = mcp.read_adc(7)
    print ("Ambient Sound  set to: ", ambientSound)
    soundTrigger = ambientSound + 150

    sql = "INSERT INTO sound_sensor(datetime1, sound_level, sensor_id) VALUES (%s,%s,%s)"
    sensor_id = 001
    # Main program loop.
    while True:
        # The read_adc function will get the value of the specified channel (7).
        sound = mcp.read_adc(7)
        print(sound)
	#Trigger if sound level is too high
	if sound < soundTrigger:
	     print "Sound level is too high\n"
	#I assume this means I'm committing only the moment I trigger the sound instead of every time I issue it
	     mydb.commit()
	     while sound < soundTriggerHigh:
		sound = mcp.read_adc(7)
		GPIO.output(13, GPIO.HIGH)
                time.sleep(2)
                GPIO.output(13, GPIO.LOW)
	     print "Sound level back to ambient level\n"
	#Stops infinite while statement to not takeover monitor.py
		break
        #this is based from the lightSensor.py file so
        ssound = str(sound)
        #variable for datetime
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #values to be inserted into sound_sensor table
        val = (current_datetime, ssound, sensor_id)
        #insert sound value into database with datetime
        mycursor.execute(sql, val)
        //print(mycursor.rowcount, "Data Recorded")
read_sound()
