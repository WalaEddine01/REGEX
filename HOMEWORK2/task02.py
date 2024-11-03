#!/bin/python3
"""
This module extract and Normalize Phone Numbers.
"""
import re

def extract_phone_numbers(text):
    """
    Extract and Normalize Phone Numbers.
    """
    pattr = r'(?:\+\d{1,3} |\+\d{1,3}-)?(?:\([0-9]{3}\)|[0-9]{3})[- .]?[0-9]{3}[ -.]?[0-9]{4}'
    phones = re.findall(pattr, text)
    normalizedNumbers = []
    
    for phone in phones:
        digits = re.sub(r'[^0-9]', '', phone)

        if len(digits) == 10:
            countryCode = '1'
            areaCode = digits[:3]
            mainNumber = digits[3:]
        else:
            countryCode = digits[:-10]
            areaCode = digits[-10:-7]
            mainNumber = digits[-7:]

        formattedNumber = f"+{countryCode} {areaCode} {mainNumber[:3]} {mainNumber[3:]}"
        normalizedNumbers.append(formattedNumber)
    
    return normalizedNumbers
    

if __name__ == "__main__":
    string = """
(555) 444-7890
555-444-7892
5554447890
555 444 7890
555.444.7890
+213 555 444 7890
+1-555-444-7890
+1 (555) 444-7890
+111 (555) 444-7890
"""
    print(extract_phone_numbers(string))