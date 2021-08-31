import calendardata
import weatherdata
import scrollphathd as sphd
import time
from datetime import datetime, timedelta



def create_infostring():
	weather_report = weatherdata.fetch()
	calendar_report = calendardata.fetch()
	infostring = f'{calendar_report} {weather_report}'
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


create_infostring()
