import datetime
import schedule
from datebot import DateBot
import weatherdata
import scrollphathd as sphd
import time


class InfoBot: 

	def __init__(self):
		self.datebot = DateBot()

	def create_infostring(self):
		sphd.clear()
		sphd.show()
		print("Creating infostring")
		weather_report = weatherdata.fetch()
		infostring = f'{self.datebot.date_string} {weather_report} '
		print(infostring)
		sphd.write_string(infostring)
		sphd.set_brightness(0.3)
		self.display_infostring

	def display_infostring(self):
		sphd.show()
		sphd.scroll(1)
	
	def update_datebot(self):
		self.datebot = DateBot()


def update_schedule_info():
	print(f'Schedule {schedule.get_jobs()}')
	

def start_infobot():
	print("Starting Infobot")
	infobot = InfoBot()
	infobot.create_infostring()
	schedule.every(1).minute.do(update_schedule_info)
	schedule.every().hour.do(infobot.create_infostring)
	schedule.every().day.at("00:00").do(infobot.update_datebot)
	while True:
		infobot.display_infostring()
		schedule.run_pending()
		time.sleep(0.03)

start_infobot()
