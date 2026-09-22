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
    pari = [(i["correct_answer"], "t")] + [(ans, "f") for ans in i["incorrect_answers"]]
    odgovori = dict(r.sample(pari, len(pari)))
    print("Možni odgovori:")

