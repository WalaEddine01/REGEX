#!/bin/python3

import re

def exo06(txt):
    pattr = r"^#\w+"
    pattr2 = r'(?<=[#])(.+)'
    return re.findall(pattr2, txt)
