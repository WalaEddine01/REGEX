import re

def exo02(text):

    pattr = '[0-9]+'

    res = re.findall(pattr, text)

    print(res)


exo02("tes3tT1")

