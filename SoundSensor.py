import threading
def read_sound():
    threading.Timer(10, read_sound).start()
    # Import SPI library (for hardware SPI) and MCP3008 library.
    import Adafruit_GPIO.SPI as SPI
    import Adafruit_MCP3008

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

    #database structure of sound sensor
	#mycursor.execute("CREATE TABLE sound_sensor(id INT(4), datetime1 DATETIME, sound_level INT(4), sensor_id)")

    sql = "INSERT INTO sound_sensor(datetime1, sound_level, sensor_id) VALUES (%s,%s,%s)"
    sensor_id = 001
    # Main program loop.
    while True:
        # The read_adc function will get the value of the specified channel (2).
        sound = mcp.read_adc(7)
        print(sound)
        #convert sound to string for the sql query //i'm not sure if this is really needed
        ssound = str(sound)
        #variable for datetime
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #values to be inserted into sound_sensor table
        val = (current_datetime, ssound, sensor_id)
        #insert sound value into database with datetime
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data Recorded")
        # Wait for 10 seconds to measure sound level again.
        time.sleep(10)
