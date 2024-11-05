import re

def exo03(text):
    pattr = r'[a-zA-Z._]+@[a-zA-Z]+\.[a-zA-Z]+'

    res = re.fullmatch(pattr, text)
    print(res != None)
    print(res)

string = "wala@wala.wala"
exo03(string)
