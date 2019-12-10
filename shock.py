def seismometer():
    import smbus			#import SMBus module of I2C
    from time import sleep          #import
    import RPi.GPIO as GPIO
    import mysql.connector
    import datetime
    import math

    #some MPU6050 Registers and their Address
    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38
    ACCEL_XOUT_H = 0x3B
    ACCEL_YOUT_H = 0x3D
    ACCEL_ZOUT_H = 0x3F
    GYRO_XOUT_H  = 0x43
    GYRO_YOUT_H  = 0x45
    GYRO_ZOUT_H  = 0x47
    TEMP_OUT     = 0x41

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)


    def MPU_Init():
        #write to sample rate register
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
        
        #Write to power management register
        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        
        #Write to Configuration register
        bus.write_byte_data(Device_Address, CONFIG, 0)
        
        #Write to Gyro configuration register
        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
        
        #Write to interrupt enable register
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(addr):
        #Accelero and Gyro value are 16-bit
            high = bus.read_byte_data(Device_Address, addr)
            low = bus.read_byte_data(Device_Address, addr+1)
        
            #concatenate higher and lower value
            value = ((high << 8) | low)
            
            #to get signed value from mpu6050
            if(value > 32768):
                value = value - 65536
            return value


    bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
    Device_Address = 0x68   # MPU6050 device address

    MPU_Init()

    #connecting the database
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="pi",
	  passwd="raspberry",
	  database="libhat"
	)
	print "connected"
	mycursor = mydb.cursor()

   

    print (" Reading Data of Gyroscope and Accelerometer")


        
    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    
    #Full scale range +/- 250 degree/C as per sensitivity scale factor
    Ax = acc_x/16384.0
    Ay = acc_y/16384.0
    Az = acc_z/16384.0
    Ar = math.sqrt(math.pow(Ax,2) + math.pow(Ay,2) + math.pow(Az,2))
    diff = math.fabs(1.025 - Ar)
    if (diff >= 0.092 ):
        print('strong earthquake')
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
    elif (diff >= 0.039):
        print('weak earthquake')
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(13, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)

    #database structure of temp and humid
	#mycursor.execute("CREATE TABLE shock(id INT(4), datetime1 DATETIME, ax FLOAT(5,3), ay FLOAT(5,3), az FLOAT(5,3), ar FLOAT(5,3))")

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO idshock(sensorid, datetime1, ax, ay, az, ar) VALUES (%s,%s,%s,%s,%s,%s)"
	sensor_id=001
	val = (sensor_id, current_datetime, Ax, Ay, Az, Ar)
	mycursor.execute(sql, val)
	mydb.commit()
        
    print ( "Ax=%.3f g | " %Ax + "Ay=%.3f g | " %Ay + "Az=%.3f g" %Az)
    time.sleep(50)
