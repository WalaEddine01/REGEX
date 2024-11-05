#!/bin/python3
import re

def exo04(text):

    pattr = r'(([1][0-2])|([0][0-9]))-(([3][0-1])|([0-2][1-9]))-([0-9]{4})'
    result = re.findall(pattr, text)
    print(result)

string = "12-01-2003ss"
exo04(string)
