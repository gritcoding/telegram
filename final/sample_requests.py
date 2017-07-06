from pprint import pprint
import requests  # http://docs.python-requests.org/en/master/user/quickstart/
import cfscrape  # https://github.com/Anorov/cloudflare-scrape  # pip3 install cfscrape

TELEGRAM_API_TOKEN = '369935459:AAGM3_yfHNmtdcSZi8QFP5pgpl24-VK6P7w'
WEATHER_API_TOKEN = '2624c50872bfb55133dae6592058d5a9'
POLLUTION_API_TOKEN = '4152717b1cf01e12812c588a310d762bea5799f1'
TRANSLATE_API_TOKEN = 'AIzaSyAuGBOw2KGYTp5eAl5k4LzQDwp_qrEEAE0'

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?APPID=%s&q=%s"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?APPID=%s&q=%s"
WEATHER_ICON_URL = "http://openweathermap.org/img/w/%s.png"
POLLUTION_URL = "http://api.waqi.info/feed/%s/?token=%s"
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2?key=%s&q=%s&source=%s&target=%s"
LANGUAGE_URL = "https://translation.googleapis.com/language/translate/v2/languages?key=%s"
POKEMON_URL = "http://pokeapi.co/api/v2/pokemon/%s/"

################################################################################

# token: http://openweathermap.org/appid
# docs:  https://openweathermap.org/api
#        https://openweathermap.org/weather-conditions
def weather(city):
    request = WEATHER_URL % (WEATHER_API_TOKEN, city)
    print(request)
    response = requests.post(request).json()
    response['icon_url'] = WEATHER_ICON_URL % (response['weather'][0]['icon'])
    #pprint(response)
    return response

def forecast(city):
    request = FORECAST_URL % (WEATHER_API_TOKEN, city)
    print(request)
    response = requests.post(request).json()
    #pprint(response)
    return response

# token: http://aqicn.org/data-platform/token/
# docs:  http://aqicn.org/api/
#        http://aqicn.org/json-api/doc/
def pollution(city):
    request = POLLUTION_URL % (city, POLLUTION_API_TOKEN)
    print(request)
    response = requests.post(request).json()
    #pprint(response)
    return response

# token: https://support.google.com/cloud/answer/6158862?hl=en
# docs:  https://cloud.google.com/translate/docs/reference/rest?authuser=1
def translate(text, source_language, target_language):
    request = TRANSLATE_URL % (TRANSLATE_API_TOKEN, text, source_language, target_language)
    print(request)
    response = requests.post(request).json()
    #pprint(response)
    return response['data']['translations'][0]['translatedText']


def languages():
    request = LANGUAGE_URL % (TRANSLATE_API_TOKEN)
    print(request)
    response = scraper.get(request).json()
    #pprint(response)
    return response

# docs:  http://pokeapi.co/docsv2/
#        https://github.com/PokeAPI/sprites/tree/master/sprites/pokemon
#        https://github.com/PokeAPI/pykemon
def pokemon(name):
    request = POKEMON_URL % (name)
    print(request)
    scraper = cfscrape.create_scraper()
    response = scraper.get(request)
    #response = requests.get(request)
    pprint(response)
    json = response.json()
    pokemon = {}
    pokemon['id'] = json['id']
    pokemon['name'] = json['name']
    pokemon['height'] = json['height']
    pokemon['weight'] = json['weight']
    pokemon['base_experience'] = json['base_experience']
    pokemon['sprite'] = json['sprites']['front_default']
    return pokemon

################################################################################

#pprint(weather("Hong Kong"))
#pprint(forecast("Hong Kong"))

#pprint(pollution("beijing"))

#pprint(translate("hello", "en", "zh"))
#pprint(languages())

# pprint(pokemon('pikachu'))

