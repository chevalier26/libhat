def read_light():
    # Import SPI library (for hardware SPI) and MCP3008 library.
    import Adafruit_GPIO.SPI as SPI
    import Adafruit_MCP3008
    import mysql.connector
    import RPi.GPIO as GPIO
    import os
    import glob
    import time
    import datetime

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

    #database structure of light sensor
    #mycursor.execute("CREATE TABLE light_sensor(id INT(4), datetime1 DATETIME, light_level INT(4), sensor_id)")
    x = 0
    #calibrating
    print "Please put sensor on ambient light to calibrate, after 5 seconds the current light level will be set to ambient"
    while x != 5:
        x += 1
        time.sleep(1)
    ambientLight = mcp.read_adc(2)
    print ("Ambient light level set to: ", ambientLight)
    lightTrigger = ambientLight + 200

    sql = "INSERT INTO light_sensor(datetime1, light_level, sensor_id) VALUES (%s,%s,%s)"
    sensor_id = 001
    # Main program loop.
    while True:
        # The read_adc function will get the value of the specified channel (2).
        light = mcp.read_adc(2)
        print(light)
	#Trigger if light level is low
	if light > lightTrigger:
            while light > lightTrigger:
                light = mcp.read_adc(2)
                print "Light level is low\n"
                GPIO.output(13, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(13, GPIO.LOW)
        #convert light to string for the sql query //i'm not sure if this is really needed
        slight = str(light)
        #variable for datetime
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #values to be inserted into light_sensor table
        val = (current_datetime, slight, sensor_id)
        #insert light value into database with datetime
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data Recorded")
        # Wait for 10 mins to measure light level again.
        time.sleep(5)
read_light()
