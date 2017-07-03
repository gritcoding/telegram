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
    greeting = "I don't know!"
    if hour > 2 and hour < 12:
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


# BONUS FEATURES:

# Your Bot is polite, but understands only one command. Perhaps it should respond to different commands.
# Get your Bot to respond when you say 'bye' or 'goodbye'.

# CLUES: You can use elif between if and else.
#        You can use 'or' between boolean tests, for example: 'bye' or 'goodbye'

# GO!

# Should you be able to say 'bye' before you've said 'hello'? Your Bot should know if you've said hello
# before it says goodbye. Your bot needs to remember what was said before.

# CLUES: Use another variable to remember if you've said hello, for example = said_hello = False
#        Then you can test if hello was said before, for example: if (said_hello), if (not said_hello)
#
#        The value of said_hello cannot change between calls to the handle() function, you need to use
#        the global value of said_hello, for example set the value of said_hello outside handle(), then
#        declare 'global said_hello' inside handle().

# GO!

# Group chat! Yes, we want our Bot to participate in a group. But how does our Bot know it's being spoken to?
# It might get confused by everyone else chatting! We solve this problem by putting a slash '/' before commands
# for the Bot. So we won't say 'hello' or 'bye', but will say '/hello' or '/bye'.

# CLUE: You can use string.startswith() to test if a string starts with a particular character.

# Give it a try! Create a group with your friends in Telegram and add your Bot. Your Bot should only respond
# to 'commands', that is messages that start with '/'.

# GO!

# Have you noticed what happens when many people try to talk to your Bot? It doesn't know who has said hello
# and who has said goodbye. Your Bot is confused! Why does this happen? Can you get your Bot to remember who
# it's been talking to and respond accordingly? What kind of variable can you use to do this?

# CLUES:You can try using a dictionary. For example:
#          said_hello = { }
#          said_hello['Alice'] = False
#          said_hello['Bob'] = False
#       Then you can test if someone has said hello, for example:
#          if (said_hello['Alice'])
#          if (not said_hello['Alice'])
#
#       You can play with dictionaries in the shell first to understand how this works.
#
#       You might want to 'initialize' or setup your dictionary first, for example:
#          if (chat_id not in said_hello):
#              hello[chat_id] = False

# GO!

# Wow! You're really making progress! Want to try another challenge?
# You can have your Bot understand multiple commands on the same line by 'splitting' the message.
# Try this in the shell (one line at a time):

'''
message = 'Hello World Kitty'
commands = message.lower().split(' ')
commands
commands[0]
commands[2]
'''

# Can you teach your Bot some new commands? For example, you might have a conversation like this:

# You: /hello
# Bot: Good Morning Alice. Nice to meet you!
# You: /address Wonderland
# Bot: Nice to meet you Alice from Wonderland. I am R2-D2 from Theed Royal Palace, Naboo.

# GO!