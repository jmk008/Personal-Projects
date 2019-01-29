#!/bin/python3

import json
import turtle
import urllib.request
import turtle
import time

#Assigning the ISS url to a variable
url = 'http://api.open-notify.org/astros.json'

#Calling the web service
response = urllib.request.urlopen(url)

#Loading json response into python data structure
result = json.loads(response.read())

#print(result)

number = result['number']

print('People in Space:',number)

people = result['people']

for p in people:
  print(p['name'] + ' in ' + p['craft'])
  
print('\n')

#ISS coordinates url
iss_url = 'http://api.open-notify.org/iss-now.json'

#Calling web service
iss_response = urllib.request.urlopen(iss_url)

#Loading json response in python data structure
iss_result = json.loads(iss_response.read())

#print(iss_result)

location = iss_result['iss_position']

#Latitude and longitude
lat = float(location['latitude'])
lon = float(location['longitude'])

#Screen for map and setting up map to dimentions
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

#Inserting the ISS image
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

#Positioning the ISS at its current location
iss.penup()
iss.goto(lon,lat)

#Finding when ISS will pass overhead my coordinates
my_lat = 42.8814 #enter your latitude
my_lon = -55.3907 #enter your longitude
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(my_lon,my_lat)
location.dot(5)
location.hideturtle()

#Overhead url
over_url = 'http://api.open-notify.org/iss-pass.json'
over_url = over_url + '?lat='+str(lat)+ '&lon=' +str(lon)
response = urllib.request.urlopen(over_url)
result = json.loads(response.read())
#print(result)

over = result['response'][1]['risetime']
#print(over)

#Getting timestamp to readable time and plotting on the map
style = ('Arial', 6 , 'bold')
location.write(time.ctime(over), font=style)