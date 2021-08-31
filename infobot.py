import schedule
import datetime
import calendardata
import weatherdata
import scrollphathd as sphd
import time

today = datetime.date.today()
day  = ""
month = ""
month_name = ""
year = ""
day_name = ""
today_date = ""
day_data = ""
day_string = ""
holiday = ""

def set_date():
	print("Setting the date")
	today = datetime.date.today()
	day  = today.strftime("%d")
	month = today.strftime("%m")
	month_name = today.strftime("%B")
	year = today.strftime("%Y")
	day_name = today.strftime('%A')
	today_date = f'{year}-{month}-{day}'
	day_string = f'{day_name} {day} {month_name} {year}'
	holiday = calendardata.get_bank_holiday(f'{year}-{month}-{day}')

def create_infostring():
	sphd.clear()
	print("Creating infostring")
	weather_report = weatherdata.fetch()
	holiday_message = calendardata.get_holiday_message(holiday)
	infostring = f'{day_string} {calendardata.get_solstice(month, day)} {holiday} {holiday_message} {weather_report} '
	print(infostring)
	display_infostring(infostring)


def display_infostring(infostring):
	sphd.clear()
	sphd.write_string(infostring)
	sphd.set_brightness(0.3)
	while True:
		sphd.show()
		sphd.scroll(1)
		time.sleep(0.03)

def start_infobot():
	set_date()
	create_infostring()
	schedule.every(1).hours.do(create_infostring)
	schedule.every().day.at("00:00").do(set_date)
	print(f'Schedule {schedule.idle_seconds()}')
	while True:
		schedule.run_pending()
		time.sleep(1)

start_infobot()
