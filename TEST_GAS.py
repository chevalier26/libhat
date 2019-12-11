from mq import *
import sys, time
import datetime

#connecting the database
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="pi",
	  passwd="raspberry",
	  database="libhat"
	)
	print "connected"
	mycursor = mydb.cursor()

	#database structure of temp and humid
	#mycursor.execute("CREATE TABLE temp_humid(id INT(5), time1 DATETIME, LPG INT(5), CO INT(5), smoke INT(5))")

	current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	sql = "INSERT INTO gas_sensor(datetime1, GAS_LPG, CO, SMOKE, sensor_id) VALUES (%s, %s, %s, %s, %s)"
	sensor_id=001



    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:

    	
        #perc = mq.MQPercentage()
        #sys.stdout.write("\r")
        #sys.stdout.write("\033[K")
        #sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"])) # value reflected from mq
        #sys.stdout.flush() 
        #time.sleep(0.1)

	
	val = (current_datetime, GAS_LPG, CO, SMOKE, sensor_id)
	#print val;
	#print sql;
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted")
	time.sleep(0.1)