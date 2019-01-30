import pygal

temp = []
pressure = []
humidity = []

#temperature
file = open('temperature.txt','r')

for line in file.read().splitlines():
    if line:
        temp.append(float(line))

file.close()

#pressure
file = open('pressure.txt','r')

for line in file.read().splitlines():
    if line:
        pressure.append(float(line))

file.close()

#humidity
file = open('humidity.txt','r')

for line in file.read().splitlines():
    if line:
        humidity.append(float(line))

file.close()

weather = pygal.Line()
weather.add('temperature (C)',temp)
#weather.add('pressure (Bars)', pressure)
weather.add('humidity (%)', humidity)
weather.title = 'Weather'
weather.x_labels = range(1, len(temp)+1)
#weather.x_labels = range(1, len(pressure)+1)
weather.x_labels = range(1, len(humidity)+1)
weather.render_to_file('chart.svg')
