def read_LPG():
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
    GPIO.setup(13, GPIO.OUT)     ####FOR LED####
    GPIO.setup(6, GPIO.OUT)      ####FOR SOUND TRIGGER####

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

    #Database connection
    mydb = mysql.connector.connect(
    	 host="localhost",
    	 user="pi",
    	 passwd="raspberry",
    	 database="libhat"
	)
    print "connected"
    mycursor = mydb.cursor()

    #database structure
    #mycursor.execute("CREATE TABLE LPG_sensor(id INT(4), datetime1 DATETIME, LPG_level INT(4), sensor_id)")
    x = 0

    #Calibration
    print "Calibrating ambient combustible gas content for 10 seconds"
    while x != 10:
        x += 1
        time.sleep(1)
    ambientLPG = mcp.read_adc(4)
    print ("LPG Room Ambient ", ambientLPG)
    lpgTrigger = ambientLPG*2 #LPG PEL = 1000ppm, IDLH = 2000 
    

    sql = "INSERT INTO LPG_sensor(datetime1, LPG_level, sensor_id) VALUES (%s,%s,%s)"
    sensor_id = 001

    # Main program loop. Adapted from lighsensor.py
    while True:
        # The read_adc function will get the value of the specified channel (2).
        LPG = mcp.read_adc(4)
        print("LPG Content ", ambientLPG)

	#Trigger for high LPG content
	if LPG < lpgTrigger:
	     print "Combustible gas level too high\n"
	     while LPG < lpgTrigger:
		LPG = mcp.read_adc(4)
		GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
               
        #String conversion
        sLPG = str(LPG)
        #variable for datetime
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #values for LPG_sensor table
        val = (current_datetime, sLPG, sensor_id)
        #insert light value into database with datetime
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data Recorded")
read_LPG()