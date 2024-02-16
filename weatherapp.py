#writing a python program for making the weather app(getting current weather, pressure, humidity etc)
#importing the modules
import requests

#Enter your api key below
api_key ="07ed2f58dbffef2ab1948281eda25f72";

#For getting the city name from the user
city_name = input("Enter city name: ");

#Base url (for getting the details from the location details)
base_url = "http://api.openweathermap.org/data/2.5/weather?";
#complete url for getting the details from the api link
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

#getting details from the app
response = requests.get(complete_url);

#getting current temperature, humidity and description
jsonData = response.json();
#print(jsonData);
if (jsonData['cod'] != 404):
    current_temperature= jsonData["main"]["temp"];
    current_humidity =jsonData["main"]["humidity"];
    current_description = jsonData["weather"][0]["description"];
else:
    print("plese Enter valid city name");

#printing temperature, humidity and description for specified city
print(city_name + " Temperature is : " + str(current_temperature))
print(city_name + " Humidity is : " + str(current_humidity))
print(city_name + " Description is : " + str(current_description))

