from temphummod import readtemphumid
from shock import seismometer
from userCount import userCount
from SoundSensor import read_sound
from lightSensor import read_light
import threading
from threading import Thread


readtemphumid()
seismometer()
#userCount()
#read_sound()
light = threading.Thread(target=read_light, args=())
light.start()
