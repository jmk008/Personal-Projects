from sense_hat import *
from time import sleep

sense = SenseHat()

count = 0

while count != 12:
    count += 1
    
    sleep(5)

    #temperature
    my_file = open('temperature.txt','a')
    my_file.write(str(sense.get_temperature()))
    my_file.write('\n')
    my_file.close()

    #pressure
    my_file = open('pressure.txt','a')
    my_file.write(str(sense.get_pressure()/1000))
    my_file.write('\n')
    my_file.close()

    #Humidity
    my_file = open('humidity.txt','a')
    my_file.write(str(sense.get_humidity()))
    my_file.write('\n')
    my_file.close()
