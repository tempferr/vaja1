import requests
# Iz seznama vaših družinskih imen
#Izpišite najstarejše ime


imena = ["erik", "mark", "borut", "natalija"]
max_starost = 0
max_ime = ""
for i in imena:
    klic = requests.get(f"https://api.agify.io?name={i}").json()
    age = klic["age"]

    if age>max_starost:
        max_starost=age
        max_ime = i
print(max_starost, max_ime)
