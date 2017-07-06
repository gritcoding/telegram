import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import requests

TELEGRAM_API_TOKEN = '369935459:AAGM3_yfHNmtdcSZi8QFP5pgpl24-VK6P7w' # Copy your token here.
WEATHER_API_TOKEN = '2624c50872bfb55133dae6592058d5a9'
POLLUTION_API_TOKEN = '4152717b1cf01e12812c588a310d762bea5799f1'

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?APPID=" + WEATHER_API_TOKEN
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?cnt=3&APPID=" + WEATHER_API_TOKEN
POLLUTION_URL = "http://api.waqi.info/feed/shanghai/?token=" + POLLUTION_API_TOKEN

bot = telepot.Bot(TELEGRAM_API_TOKEN)

def handle(message):
    pprint(message)
    print()
    content_type, chat_type, chat_id = telepot.glance(message)
    
    if content_type == "text":
        text = message['text']
        bot.sendMessage(chat_id, text)
    else:
        bot.sendMessage(chat_id, "I don't understand!")

#MessageLoop(bot, handle).run_as_thread()
        
request = WEATHER_URL + "&q=Hong Kong"
response = requests.get(request).json()

pprint(response)

request = FORECAST_URL + "&q=Hong Kong"
response = requests.get(request).json()

pprint(response)

request = POLLUTION_URL + "&q=Hong Kong"
response = requests.get(request).json()

pprint(response)

        
