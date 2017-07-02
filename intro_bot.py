# Same as before, follow the instructions and when you see 'GO!', save and run the file

import telepot
from pprint import pprint

# 'import' lets you use even more functions. These imports help us talk to our bot.

API_TOKEN = # Copy your token here.

bot = telepot.Bot(API_TOKEN)
me = bot.getMe()
print (me)

# GO!

# telepot.Bot() connects to your Bot.
# getMe() returns a dictionary with information about your Bot.

# Try printing only the username of your bot.

# print (me['username'])

# GO!

# Now let's get to chatting! Say something to your Bot and then print it out.

# messages = bot.getUpdates()
# print(messages)

# GO!

# The message is also a dictionary (an array of dictionaries), but hard to read.
# pprint() makes it a little easier to read your dictionary.

# pprint(messages)

# Take note of the structure of the messages. Can you see who it's coming from? Can you see the text?
# Try sending an image and see what happens (raspberry.jpg).

# Now let's have our Bot say something!

# user_id = # paste user's id
# bot.sendMessage(user_id, "I love raspberries!")

# GO!

# Say something more interesting.

# first_name = # user's name
# message = "Hello " + first_name + ". Great day for eating raspberries!"
# bot.sendMessage(message)

# GO!

# Ooops! Did we make a mistake? Can you fix it?

# CLUE: who do we need to send the message to?
