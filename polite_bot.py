# Same as before, follow the instructions and when you see 'GO!', save and run the file

import telepot
from telepot.loop import MessageLoop
from pprint import pprint

API_TOKEN = # Copy your token here.
bot = telepot.Bot(API_TOKEN)

def handle(message):
    pprint(message)
    print()
    content_type, chat_type, chat_id = telepot.glance(message)
    
    if content_type == "text":
        text = message['text']
        bot.sendMessage(chat_id, text)
    else:
        bot.sendMessage(chat_id, "I don't understand!")

MessageLoop(bot, handle).run_as_thread()

# Here's our simple Parrot Bot again. Let's make sure it works.

# GO!


# Shouldn't our Bot be a little smarter than a parrot? Let's teach it some manners!

# When we say 'hello' to our bot, it should reply with: 'Hello <your name>. Nice to meet you!'
# What should it do when we don't say hello?

'''
        from_name = message['from']['first_name']
        if text == 'hello':
            reply = # some code here
            bot.sendMessage(chat_id, reply)
        else:
            bot.sendMessage(chat_id, "Please say hello.")
'''

# GO!

# NOTE: how did we get the first name of the chat user?
#       This is a 'nested' dictionary, and it's easy to use when you know how!

# But our bot it not as polite as it should be. What happens if you say 'Hello'?
# Or if you say 'HELLO'?  Shouldn't our bot be a little smarter?

# Try this in the shell (one line at a time):

'''
text = 'Hello'

text
text.lower()

text == 'hello'
text.lower == 'hello'
'''

# Now change your code to understand hello even if there are some capital letters.

# GO!


# A truly polite Bot will know when to say 'Good morning', 'afternoon', or 'evening'.

# First we will need to import the functions for datetime.
# Copy this at the top of the file with other imports:

# import datetime

# GO!

# Now try the following in the shell (one line at a time):

'''
now = datetime.datetime.now()
now

now.hour
'''

# Do you think you can use the hour to determine whether it is morning, afternoon or evening?
# Write a function to do this:

'''
def time_of_day():
    hour = # get the hour of the day
    greeting = 'I don't know!'
    if hour > 2 and hour <= 12:
        greeting = 'Good morning'
    elif #something:
        greeting = 'Good afternoon'
    else:
        greeting = # what is left?
    return greeting
'''

# And then call your function when setting the reply (you can test your function in the shell first!):

# reply = time_of_day() + # etc etc

# GO!

# NOTE: We are using 'and' to combine boolean tests.
#       We are also using if, elif, else for multiple conditions.
