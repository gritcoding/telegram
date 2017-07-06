import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import datetime

API_TOKEN = # Copy your token here.
bot = telepot.Bot(API_TOKEN)

hello = { }

def handle(message):
    pprint(message)
    content_type, chat_type, chat_id = telepot.glance(message)

    global hello
    if (chat_id not in hello):
        hello[chat_id] = False
    
    if content_type == "text":
        text = message['text']
        if (text.startswith('/')):
            from_name = message['from']['first_name']
            if text.lower() == '/hello':
                if (not hello[chat_id]):
                    reply = time_of_day() + from_name + ". Nice to meet you!"
                    hello[chat_id] = True
                else:
                    reply = 'You have already said hello!'
            elif text.lower() == '/bye' or text.lower() == '/goodbye':
                if (hello[chat_id]):
                    reply = "Goodbye! Please come again."
                    hello[chat_id] = False
                else:
                    reply = "Please say hello first!"
            else:
                reply = "Please say hello or bye."
        else:
            reply = ''
    else:
        reply = "I don't understand!"
        
    if (reply):
        bot.sendMessage(chat_id, reply)
    pprint(hello)
    print()
    return

MessageLoop(bot, handle).run_as_thread()

def time_of_day():
    hour = datetime.datetime.now().hour
    greeting = "I don't know!"
    if hour > 2 and hour < 12:
        greeting = 'Good morning '
    elif hour >= 12 and hour < 6:
        greeting = 'Good afternoon '
    else:
        greeting = 'Good evening '
    return greeting