import os
import my_apis
from requests import get
from pprint import  pprint
import json
import datetime


# weatherdata makes a call to the Open Weather API
# Substitute the LATITUDE, LONGITUDE and YOUR_API_ID values in the url below
# https://api.openweathermap.org/data/2.5/onecall?lat=<LATITUDE>&lon=<LONGITUDE>&units=metric&appid=<YOUR_API_ID>

url = my_apis.weather_api()

def format_time(time):
	return datetime.datetime.utcfromtimestamp(time).strftime('%H:%M:%S')

def rain_forecast(rain_for_the_hour):
	for chance_of_rain in rain_for_the_hour:
		time = chance_of_rain.get('dt')
		chance = chance_of_rain.get('precipitation')
		if chance != 0: 
			time_of_rain = format_time(time)
			return(f'{chance}mm of rain at {time_of_rain}')
	return("no rain expected")

def get_temperature(current_weather):
	current_temperature = f"temperature: {str(current_weather['temp'])}{chr(176)}C" 
	feels_like = f"feels like: {str(current_weather['feels_like'])}{chr(176)}C" 
	return current_temperature + " " + feels_like

def calculate_moon(moon_phase):
	if moon_phase == 0 or moon_phase == 1 :
		return 'new moon' 
	elif moon_phase > 0 and moon_phase < 0.25:
		return 'waxing crescent'
	elif moon_phase == 0.25:
		return 'first quarter'
	elif moon_phase > 0.25 and moon_phase < 0.5:
		return 'waxing gibbous'
	elif moon_phase == 0.5:
		return 'full moon lyncanthropy index: howling'
	elif moon_phase > 0.5 and moon_phase < 0.75:
		return 'waning gibbous'
	elif moon_phase == 0.75:
		return 'last quarter'
	elif moon_phase > 0.75 and moon_phase < 1:
		return 'waning crescent'  

def get_sun_and_moon(daily_weather):
	pprint("DAILY")
	daily_data = daily_weather[0]
	sunrise = format_time(daily_data['sunrise'])
	sunset = format_time(daily_data['sunset'])
	moonrise = format_time(daily_data['moonrise'])
	moonset = format_time(daily_data['moonset'])
	moon_phase = calculate_moon(daily_data['moon_phase'])
	return f'sunrise: {sunrise} sunset {sunset} moonrise {moonrise} moonset {moonset} moon phase: {moon_phase}'

def get_misc_weather(weather):
	pprint(weather)
	uvi = weather.get('uvi')
	humidity = weather.get('humidity')
	dew_point = weather.get('dew_point')
	pressure = weather.get('pressure')
	visibility = weather.get('visibility')
	wind_speed = weather.get('wind_speed')
	clouds = weather.get('clouds')
	return f'UV index: {uvi} humidity: {humidity}% dew point: {dew_point}{chr(176)} wind_speed: {wind_speed} atmospheric pressure at sea level {pressure}hPa visibility: {visibility} metres cloud cover: {clouds}%'



def fetch():
	weather_update = get(url).json()
	current_weather = weather_update['current']
	rain = rain_forecast(weather_update['minutely'])
	weather_description = current_weather['weather']
	temperature = get_temperature(current_weather)
	sun_and_moon = get_sun_and_moon(weather_update['daily'])
	misc_weather = get_misc_weather(weather_update['current'])
	verbose_description = weather_description[0].get('description')
	simple_description = weather_description[0].get('main')
	weather_report = f'{verbose_description} {rain} {temperature} {sun_and_moon} {misc_weather}'
	pprint(weather_report)
	return weather_report





