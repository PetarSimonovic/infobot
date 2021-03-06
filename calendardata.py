from pymeeus.Sun import Sun
import datetime
from requests import get
import json
import pprint
import random

bank_holidays_API = get('https://www.gov.uk/bank-holidays.json').json()

def calculate_solstice(target, event, day):
	year = datetime.datetime.now().year
	solstice = Sun.get_equinox_solstice(year, target=target)
	y, m, d, h, mi, s = solstice.get_full_date(utc=True)
	solstice_day = f'{d}'
	if solstice_day == day:
		print("It's a solstice or equinox")
		print(h)
		print(mi)
		solstice_time = f'at {h}:{mi}'
		solstice_text = (f'the {target} {event} will take place today at {solstice_time} UTC')
		return solstice_text
	else:	
		return ""

def get_solstice(month, day):
	if month == "03": 
		return calculate_solstice("spring", "equinox", day)
	elif month == "06": 
		return calculate_solstice("summer", "solstice", day)
	elif month == "09": 
		return calculate_solstice("autumn", "equinox", day)
	elif month == "12":
		return calculate_solstice("winter", 'solstice', day)
	else:
		return ""

def get_bank_holiday(today):
	print(today)
	year = datetime.datetime.now().year
	if today == f'{year}-10-31':
		return "Halloween"
	elif today == f'{year}-12-24':
		return "Christmas Eve"
	elif today == f'{year}-12-25':
		return "Christmas Day"
	elif today == f'{year}-08-08':
		return "International Cat Day"
	bank_holidays = bank_holidays_API.get('england-and-wales')
	events = bank_holidays.get('events')
	for event in events:
		if event['date'] == today:
			return event['title']
	return ""

def santa_tracker():
	return "Santa is in the North Pole"

def get_scare():
	return random.choice([
	"Did you hear that?",
	"There's someone behind you",
	"Can you feel a ... presence?",
	"I'm pretty sure I'm haunted",
	"Something was scratching at the door",
	"I wouldn't go outside tonight",
	])

def get_joke():
	return random.choice([
	"What is Santa’s favourite kind of pizza? One that’s deep-pan, crisp and even",
	"What do Santa’s little helpers learn at school? The elf-abet!",
	"What is the best Christmas present in the world? A broken drum, you just can’t beat it!"
	])

def get_holiday_message(holiday):
	if holiday == 'Christmas Eve':
		return santa_tracker()
	elif holiday == 'Christmas Day':
		return f'Merry Christmas {get_joke()}'
	elif holiday == 'Halloween':
		return f'Happy Halloween {get_scare()}'
	elif holiday == "New Year's Day":
		return f"Happy New Year have a great {year}"
	else:
		return ""
