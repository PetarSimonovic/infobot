import datetime
import json
from requests import get
from pymeeus.Sun import Sun
from pymeeus.Epoch import Epoch

year = datetime.datetime.now().year
target="winter"


winter_solstice =  Sun.get_equinox_solstice(year, target="winter")
summer_solstice = Sun.get_equinox_solstice(year, target="summer") 

y, m, d, h, mi, s = winter_solstice.get_full_date()
print(f'{y}{m}{d}')

today = datetime.date.today()

day  = today.strftime("%d")
month = today.strftime("%m")
month_name = today.strftime("%B")
year = today.strftime("%Y")
day_name = today.strftime('%A')  
today_date = f'{year}{month}{day}'
print(today_date)



calendar_data = f'{day_name} {day} {month} {year}'

print(calendar_data)

def fetch():
	bank_holidays = get(bank_holiday_url).json
	print(bank_holidays)


