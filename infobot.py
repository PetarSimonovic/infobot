import calendardata
import weatherdata
import scrollphathd as sphd
import time

weather_report = weatherdata.fetch()

calendar_report = calendardata.fetch()

infostring = f'{calendar_report} {weather_report}'
print(infostring)


sphd.write_string(infostring)
sphd.set_brightness(0.3)

while True:
	sphd.show()
	sphd.scroll(1)
	time.sleep(0.03)

