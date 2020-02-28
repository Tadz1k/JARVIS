import datetime
from bs4 import BeautifulSoup
import requests
import re


def select_function(function):
    functions_dictionary = {"czas": 0, "data": 1, "jak masz na imię": 2, "jaka jest pogoda": 3, "wikipedia": 4, "cena": 5}
    function_id = functions_dictionary.get(function)
    if function_id == 0:
        response = time()
        return response
    elif function_id == 1:
        response = date()
        return response
    elif function_id == 2:
        response = introduce()
        return response
    elif function_id == 3:
        response = weather_here()
        return response
    elif function_id == 4:
        ask("Czego szukasz?")
        text = get_input()
        wiki_info = wiki_search(text)
        return wiki_info


def time():
    response = "jest godzina {}".format(datetime.datetime.now().strftime("%H:%M"))
    return response


def date():
    response = "dziś jest {}".format(datetime.datetime.now().strftime("%d.%m.%Y"))
    return response


def introduce():
    from json_loader import JsonLoader
    loader = JsonLoader()
    introduces = loader.load_introduces()
    responses = len(introduces)
    import random
    number = random.randint(0, responses - 1)
    for k, val in introduces:
        if int(k) == number:
            return str(val)
            break


def weather_here():
    import pyowm
    import geocoder
    import socket
    #pobieranie nazwy miasta
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    g = geocoder.ip(IPAddr)
    g = geocoder.ip('me')

    owm_api = pyowm.OWM('489a378ebf62bdada35877e1c9080598')
    observation = owm_api.weather_at_coords(g.lat, g.lng)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    humidity = w.get_humidity()
    wind = w.get_wind()
    direction = wind_direction(int(wind['deg']))
    response = """W Twojej lokalizacji {} jest {} stopni ciepła, wilgotność na poziomie {} %.
                  Wiatr wieje z prędkością około {} km/h, kierunek: {}"""\
        .format(g.city, round(temperature['temp']), humidity, round(wind['speed']), direction)
    return response


def wind_direction(deg):
    print(deg)
    if 0 < deg <= 30:
        response = "południowy."
    elif 30 < deg <= 70:
        response = "południowo wschodni."
    elif 70 < deg <= 110:
        response = "wschodni."
    elif 110 < deg <= 160:
        response = "północno wschodni."
    elif 160 < deg <= 210:
        response = "północny."
    elif 210 < deg <= 250:
        response = "północno zachodni."
    elif 250 < deg <= 290:
        response = "zachodni."
    elif 290 < deg <= 330:
        response = "południowo zachodni"
    elif 330 < deg <= 360:
        response = "południowy"
    return response


def wiki_search(text):
    import wikipedia
    wikipedia.set_lang("pl")
    return wikipedia.summary(text, 2)


def ask(question):
    from google_request import Google
    voice = Google()
    voice.request(question)


def get_input():
    print("sprawdzam")
    from voice_recognition import Recognition
    recognition = Recognition()
    text = recognition.listen()
    return text


def price_checker(item_name):
    item_name = item_name.replace(" ", "-")
    url = "https://m.ceneo.pl/;szukaj{};0115-1.htm".format(item_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    price = soup.findAll("span", {"class": "price-int"})
    name = soup.findAll("div", {"class": "list-prod-name"})
    output_price = price[1].text
    output_name = name[1].text
    output = "Znalazłem przedmiot o nazwie {} a jego cena rozpoczyna się od {}zł".format(output_name, output_price)
    #output = "{} {}".format(output_name, output_price)
    return output
