from pymeeus.Sun import Sun
import datetime
from requests import get
import json
import pprint
import random

class DateBot:


	bank_holidays_API = get('https://www.gov.uk/bank-holidays.json').json()

	def __init__(self):
		self.today = today = datetime.date.today()
		self.day  = today.strftime("%d")
		self.month = today.strftime("%m")
		self.month_name = today.strftime("%B")
		self.year = today.strftime("%Y")
		self.day_name = today.strftime('%A')	
		self.date_string = f'{self.day_name} {self.day} {self.month_name} {self.year}'
 
		
	

