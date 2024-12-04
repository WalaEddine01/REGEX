import re

def exo03(text):
    pattr = r'^[a-zA-Z._]+@[a-zA-Z]+\.[a-zA-Z]+$'

    res = re.findall(pattr, text)
    return res
