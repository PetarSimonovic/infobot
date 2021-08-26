from requests import get
import json
from pprint import pprint

url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={2a023107a3b3e33aea09afb695430413}'

stations = get(url).json()['items']

pprint(stations)
PI2a023107a3b3e33aea09afb695430413

