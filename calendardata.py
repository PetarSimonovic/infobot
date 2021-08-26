import datetime
from requests import get
import json
import pprint
import random
from pymeeus.Sun import Sun
from pymeeus.Epoch import Epoch


today = datetime.date.today()
day  = today.strftime("%d")
month = today.strftime("%m")
month_name = today.strftime("%B")
year = today.strftime("%Y")
day_name = today.strftime('%A')
today_date = f'{year}{month}{day}'
day_data = f'{day_name} {day} {month_name} {year}'
bank_holidays_API = get('https://www.gov.uk/bank-holidays.json').json()


def calculate_solstice(target):
	year = datetime.datetime.now().year
	solstice = Sun.get_equinox_solstice(year, target=target)
	y, m, d, h, mi, s = solstice.get_full_date(utc=True)
	solstice_date = (f'{y}{m}{d}')
	solstice_day = f'{d}'
	print(solstice_date)
	solstice_time = (f'at {h}:{mi}')
	print(solstice_time)
	print(today_date)
	print(day + solstice_day)
	print(month)
	if solstice_day == day:
		return solstice_time

def get_solstice():
	if month == "03":
		return f'the vernal equinox will take place today at {calculate_soltice("spring")} UTC'
	elif month == "06":
		return f'the summer solstice will take place today at {calculate_solstice("summer")} UTC'
	elif month == "09":
		return f'the autumnal equinox will take place today at {calculate_solstice("autumn")} UTC'
	elif month == "12":
		return f'the winter solstice will take place today at {calculate_solstice("winter")} UTC'
	else:
		return ""

def get_bank_holiday(today):
	print(today)
	if today == f'{year}-10-31':
		return "Halloween"
	elif today == f'{year}-12-24':
		return "Christmas Eve"
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
	"What is Santa’s favourite kind of pizza? One that’s deep-pan, crisp and even"
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

def fetch():
        scare = False
        solstice = get_solstice()
        holiday = get_bank_holiday(f'{year}-{month}-{day}')
        holiday_message = get_holiday_message(holiday)
        day_data = f'{day_name} {day} {month_name} {year}'
        solstice = get_solstice()
        calendar_report = f'{day_data} {holiday} {holiday_message} {solstice}'
        print(calendar_report)
        return calendar_report
