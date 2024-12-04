import re

def exo02(text):

    pattr = '[0-9]+'

    res = re.findall(pattr, text)
    return res

