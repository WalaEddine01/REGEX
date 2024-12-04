#!/bin/python3
import re

def exo01(text):
    patr = '^[a-zA-Z]+$'
    res = re.findall(patr, text)
    return res
