#!/bin/python3

import re

def exo07(text):
    pattrn = "[A-Z][\w]+"
    res = re.findall(pattrn, text)
    print(res)

exo07("Hello World")
