import requests
import random as r
# Naredi kviz z 10 vprašanji in nakoncu izpiše rezultat

stUprasanj = int(input("Koliko vprašanj hočete: "))
print()
urlTravia = f"https://opentdb.com/api.php?amount={stUprasanj}&type=multiple"
kt = requests.get(urlTravia).json()
for i in kt["results"]:
    print(i["question"])
    print()
    odgovori = {i["correct_answer"]: "t", i["incorrect_answers"][0] : "f", i["incorrect_answers"][1] : "f", i["incorrect_answers"][2] : "f"}
    vrstniRed = ""



# shuffle za slovarje:  promesan_slovar = dict(random.sample(list(moj_slovar.items()), len(moj_slovar)))