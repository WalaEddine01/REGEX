#!/bin/python3

import re

def exo05(text):
    pattr = r"([a-zA-Z0-9\W]{8,})+"

    result = re.findall(pattr, text)
    return result