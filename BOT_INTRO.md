# Telegram and Bot Introduction

## Login to Telegram and Create a bot

* Web interface: https://web.telegram.org
  * Using the web interface will make programming and testing a little easier.
* Connect to BotFather: https://telegram.me/botfather (open in Telegram Web)
* `/help` to see commands you can give BotFather.
* `/newbot` to create a new Bot.
  * You can name your Bot whatever you like!
  * The username of your Bot must end in 'bot'.
  * Copy the 'token' and keep it safe. We will use this token to connect to our Bot using python code!
  * More intructions here: https://core.telegram.org/bots#6-botfather
* Start chatting with your Bot.
  * Search for your Bot by name (or username to be more specific).
  * Select your Bot to start chatting.
  * Not very chatty? Let's fix that by programming it!

## Python

* We will use the *Telepot* Python framework for programming our bot.
  * If not already installed: `sudo pip3 install telepot`
  * Introduction, Reference and Examples: https://github.com/nickoala/telepot
* Open [intro_bot.py](intro_bot.py). Follow instructions. Make magic happen!

## Parrot Bot

* Now we will teach our Bot to talk back, with bells and whistles.
* Open [parrot_boy.py](parrot_bot.py)

## Polite Bot (optional)

* Our Bot can be smarter. 
* Open [polite_bot.py](polite_bot.py)
