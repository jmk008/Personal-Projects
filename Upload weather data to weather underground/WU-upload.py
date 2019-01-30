import requests
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


#Function to convert hPa to inches
def hpa_to_inches(pressure_in_hpa):
        pressure_in_inches_of_m = pressure_in_hpa * 0.02953
        return pressure_in_inches_of_m


#Function to convert rainfall in mm to inches
def mm_to_inches(rainfall_in_mm):
        rainfall_in_inches = rainfall_in_mm * 0.0393701
        return rainfall_in_inches


#Function to convert C to F since sensehat returns in C and underground
# weather station takes temp in F
def degc_to_degf(temperature_in_c):
        temperature_in_f = (temperature_in_c * (9/5.0)) + 32
        return temperature_in_f


#Convert km/h to m/h
def kmh_to_mph(speed_in_kmh):
        speed_in_mph = speed_in_kmh * 0.621371
        return speed_in_mph


# create a string to hold the first part of the URL
WUurl = "https://weatherstation.wunderground.com/weatherstation\
/updateweatherstation.php?"
WU_station_id = "KVAFAIRF147" # Replace XXXX with your PWS ID
WU_station_pwd = "tr2sglbj" # Replace YYYY with your Password
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"

while True:
        #weather parameters
        humidity = sense.get_humidity()
        ambient_temp = sense.get_temperature()
        pressure = sense.get_pressure()
        #ground_temp = 16.345
        #wind_speed = 5.6129
        #wind_gust = 12.9030
        #wind_average = 180
        #rainfall = 1.270


        #formatting data to 2 decimal places
        ambient_temp_str = "{0:.2f}".format(degc_to_degf(ambient_temp))
        #ground_temp_str = "{0:.2f}".format(degc_to_degf(ground_temp))
        humidity_str = "{0:.2f}".format(humidity)
        pressure_str = "{0:.2f}".format(hpa_to_inches(pressure))
        #wind_speed_mph_str = "{0:.2f}".format(kmh_to_mph(wind_speed))
        #wind_gust_mph_str = "{0:.2f}".format(kmh_to_mph(wind_gust))
        #wind_average_str = str(wind_average)
        #rainfall_in_str = "{0:.2f}".format(mm_to_inches(rainfall))


        #creating a request
        r= requests.get(
            WUurl +
            WUcreds +
            date_str +
            "&humidity=" + humidity_str +
            "&baromin=" + pressure_str +
            #"&windspeedmph=" + wind_speed_mph_str +
            #"&windgustmph=" + wind_gust_mph_str +
            "&tempf=" + ambient_temp_str +
            #"&rainin=" + rainfall_in_str +
            #"&soiltempf=" + ground_temp_str +
            #"&winddir=" + wind_average_str +
            action_str)

        #success if 200 code received
        print("Received " + str(r.status_code) + " " + str(r.text))

        sleep(300)


