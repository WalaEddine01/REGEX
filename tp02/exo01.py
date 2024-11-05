import re

def exo01(text):
    patr = '^[a-zA-Z]+$'
    res = re.search(patr, text)
    print(res != None)
    print(res)

String = "2ThisIs"
exo01(String)
