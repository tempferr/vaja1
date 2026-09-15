# Slovarji (dictionary) - JSON
"""
slovar = {}
print(type(slovar))
#"ključ" : "vrednost"
raznoliki = {"starost" : 17,
             "ime" : "Erik",
             "seznam" : [1,2,3,4],
             "slovar" : {"firma" : "koenigsegg", "moč" : 1200}}

# Dostop do slovarja
print(raznoliki["starost"])
print(raznoliki["slovar"])

# slovar.get("ključ", "ne najdem ključa")
print(raznoliki.get("krneki", "ne najdem ključa"))
"""

import requests

baseUrl = "https://api.open-meteo.com/v1/forecast"
params = {"latitude" :46.4682, 
          "longitude" : 13.7144,
          "daily" : "temperature_2m_max,temperature_2m_min,temperature_2m_mean",
          "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
          "forecast_days" : 1}
#latitude=46.4682&longitude=13.7144&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&current=temperature_2m&timezone=Europe%2FBerlin

call = requests.get(baseUrl, params=params)
print(call.url)
toJson = call.json()

#Trenutna temperatura
print(toJson["current"]["temperature_2m"])

#Temperature za naslednjih 7 dni

