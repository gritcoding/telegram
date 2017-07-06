import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import requests
from sample_requests import weather
from sample_requests import pollution
from sample_requests import translate
from sample_requests import pokemon

TELEGRAM_API_TOKEN = '369935459:AAGM3_yfHNmtdcSZi8QFP5pgpl24-VK6P7w' # Copy your token here.

bot = telepot.Bot(TELEGRAM_API_TOKEN)

def handle(message):
    pprint(message)
    print()
    content_type, chat_type, chat_id = telepot.glance(message)
    
    if content_type == "text":
        text = message['text'].lower().split(' ')
        
        if text[0] == '/weather':
            if len(text) == 1:
                location = "Hong Kong"
            else:
                location = message['text'].split(' ', 1)[1]
            response = weather(location)
            bot.sendMessage(chat_id, "*%s, %s* \n temperature %s \n humidity %s \n %s" % (response['name'], response['sys']['country'], response['main']['temp'], response['main']['humidity'], response['weather'][0]['description']), 'Markdown')
            bot.sendPhoto(chat_id, response['icon_url'])
        
        elif text[0] == '/pollution':
            if len(text) == 1:
                location = "Hong Kong"
            else:
                location = message['text'].split(' ', 1)[1]
            response = pollution(location)
            bot.sendMessage(chat_id, "*%s* %s" % (response['data']['city']['name'], response['data']['aqi']), 'Markdown')
        
        elif text[0] == '/translate':
            if len(text) == 1:
                q = "what?"
            else:
                q = message['text'].split(' ', 1)[1]
            response = translate(q, "en", "zh")
            bot.sendMessage(chat_id, response)

        elif text[0] == '/pokemon':
            if len(text) == 1:
                bot.sendMessage(chat_id, "Which Pokemon?")
            else:
                p = message['text'].split(' ', 1)[1]
                response = pokemon(p)
                pprint(response)
                bot.sendMessage(chat_id, "*%s* \n weight %s \n height %s \n experience %s" % (response['name'], response['weight'], response['height'], response['base_experience']), 'Markdown')
                bot.sendPhoto(chat_id, response['sprite'])
        else:
            bot.sendMessage(chat_id, "I don't understand!")
    else:
        bot.sendMessage(chat_id, "I don't understand!")

MessageLoop(bot, handle).run_as_thread()
