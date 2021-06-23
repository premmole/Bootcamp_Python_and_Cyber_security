import requests
#import os
from datetime import datetime

api_key = '56ad30ba814f3771492e5230de2312e9'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_link)
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

#The below code is to save collected info into a file
fileName = open('weatherreport.txt','a')
temp_city1 = str(temp_city)
hmdt1 = str(hmdt)
wind_spd1 = str(wind_spd)
date_time1 = str(date_time)
fileName.write("\n-------------------------------------------------------------\nWeather Stats for :"+location+" || "+date_time1+"\n-------------------------------------------------------------"+'\n')
fileName.write("Current temperature is: "+temp_city1+' deg C \n')
fileName.write("Current weather desc  : "+weather_desc+'\n')
fileName.write("Current Humidity      : "+hmdt1+'\n')
fileName.write("Current wind speed    : "+wind_spd1+'\n')


