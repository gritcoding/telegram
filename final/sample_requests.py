from pprint import pprint
import requests  # http://docs.python-requests.org/en/master/user/quickstart/

TELEGRAM_API_TOKEN  = #
WEATHER_API_TOKEN   = # 
POLLUTION_API_TOKEN = # 
TRANSLATE_API_TOKEN = # 

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?APPID=" + WEATHER_API_TOKEN
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?cnt=3&APPID=" + WEATHER_API_TOKEN
POLLUTION_URL = "http://api.waqi.info/feed/shanghai/?token=" + POLLUTION_API_TOKEN
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2?key=" + TRANSLATE_API_TOKEN
LANGUAGE_URL = "https://translation.googleapis.com/language/translate/v2/languages?key=" + TRANSLATE_API_TOKEN
POKEMON_URL = "http://pokeapi.co/api/v2/pokemon/"

################################################################################

# token: http://openweathermap.org/appid
# docs:  https://openweathermap.org/api
#        https://openweathermap.org/weather-conditions
def weather(city):
    
    return

def forecast(city):
    
    return

# token: http://aqicn.org/data-platform/token/
# docs:  http://aqicn.org/api/
#        http://aqicn.org/json-api/doc/
def pollution(city):
    
    return

# token: https://support.google.com/cloud/answer/6158862?hl=en
# docs:  https://cloud.google.com/translate/docs/reference/rest?authuser=1
#        https://translation.googleapis.com/language/translate/v2/languages?key=
def translate(text, source_language, target_language):
    request = TRANSLATE_URL + "&q=" + text + "&source=" + source_language + "&target=" + target_language
    print(request)
    response = requests.post(request).json()
    pprint(response)
    return response['data']['translations'][0]['translatedText']


def languages():
    request = LANGUAGE_URL
    print(request)
    response = requests.get(request).json()
    #pprint(response)
    return response

# docs:  http://pokeapi.co/docsv2/
#        https://github.com/PokeAPI/sprites/tree/master/sprites/pokemon
#        https://github.com/PokeAPI/pykemon
def pokemon(name):
    request = POKEMON_URL + name
    print(request)
    response = requests.get(request)
    pprint(response)
    return response

################################################################################

pprint(translate("hello", "en", "zh"))
pprint(languages())

#pokemon('pikachu')

