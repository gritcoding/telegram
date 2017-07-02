# Same as before, follow the instructions and when you see 'GO!', save and run the file

import telepot
from telepot.loop import MessageLoop
from pprint import pprint

API_TOKEN = # Copy your token here.
bot = telepot.Bot(API_TOKEN)

# In the previous exercise we learned how to get messages, but we don't need all the messages.
# We only need the most recent (last) message.
# In this exercise we will loop through messages as they are sent to our bot.

def handle(message):
    pprint(message)
    print()

MessageLoop(bot, handle).run_as_thread()

# GO!

# You can easily get some information about your message by 'glancing' at it.
# Copy the following code into your handle function above:

'''
    content_type, chat_type, chat_id = telepot.glance(message) #
    print(content_type)
    print(chat_type)
    print(chat_id)
'''

# GO!

# Try sending an image. See how the type changes.

# NOTE: The glance() function returns three values. Pretty neat!
#       If that doesn't make sense, try printing telepot.glance(message)

# Can you print the message text? Remember how to get a value from a dictionary?

# GO!


# Now let's write a PARROT BOT! A parrot repeats everything we say.
# After getting the user_id and the text of the message, send it back!

# bot.sendMessage(chat_id, text)

# What happens if you send your Parrot Bot an image (not text)?

# GO!

# Your bot doesn't know what to do! Oops.

# In programming this is called a 'bug'. We have a bug when something unexpected happens and
# our code doesn't do what we want it to do or expect it to do.

# But we can fix it! By telling our bot what to expect and then do the right thing.

# We want our bot to parrot we say only if the content_type is 'text'. Can you write code to do this?

'''
    if content_type == # what should it be?
        # let's be a parrot!
    else:
        bot.sendMessage(chat_id, "Squak! I don't understand!")
'''        

# NOTE: to test if something is equal we use == not = (test equality vs. setting value of a variable). 

# GO!

# Express your Parrot Bot's frustration when the message is not understood:

#        bot.sendPhoto(chat_id, "https://vignette4.wikia.nocookie.net/angrybirds/images/c/c9/Hal_240.png")

# GO!

# For even greater emphasis:

#        bot.sendAudio(chat_id, "http://www.flashkit.com/imagesvr_ce/flashkit/soundfx/Creatures/Birds/Bird_sc-TRD-8405/Bird_sc-TRD-8405_hifi.mp3")

# GO!
