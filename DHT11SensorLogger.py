import Adafruit_DHT
import time

interval = int(input("Please input the total minutes to wait between each log: "))

currenttime = time.localtime(time.time())

f = open("log.txt", "a")
f.write("----NEW LOG BEGIN [" + str(currenttime.tm_hour) + ":" + str(currenttime.tm_min) + "] ----\n")

try:
    while(True):
        currenttime = time.localtime(time.time())
        f = open("log.txt", "a")
        currenttime = time.ctime(time.time())
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 3)
        f.write("[" + currenttime + "] Humidity = {0:0.2f}% Temperature = {1:0.2f}c\n".format(humidity, temperature))
        time.sleep(1)
        f.close()
    
except KeyboardInterrupt:
    f.close()
