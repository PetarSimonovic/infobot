import datetime
import json
from requests import get
from pymeeus.Sun import Sun
from pymeeus.Epoch import Epoch


today = datetime.date.today()
day  = today.strftime("%d")
month = today.strftime("%m")
month_name = today.strftime("%B")
year = today.strftime("%Y")
day_name = today.strftime('%A')  
today_date = f'{year}{month}{day}'


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
		return f'the autumnal equinox will take place today at {calculate_solstice("autumn") UTC}'
	elif month == "12":
		return f'the winter solstice will take place today at {calculate_solstice("winter")} UTC'
	else:
		return ""	

def fetch():
	solstice = get_solstice()
	calendar_data = f'{day_name} {day} {month} {year}'
	calendar_report = calendar_data + get_soltice
	print(calendar_report)
	return calendar_report
