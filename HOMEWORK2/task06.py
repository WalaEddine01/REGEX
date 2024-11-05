#!/bin/python3
"""
Extract Important Dates
"""
import re
from task03 import extract_dates

def ind_upcoming_events(text, year):
    """
    This function extracts important dates from a text.
    """
    pattrn = r'(.+)(?<=(?:\s2024))'
    dates = extract_dates(text)
    date = ""
    for date in dates:
        res = re.findall(pattrn, date)
        date = res
    return (re.findall(pattrn, text))

if __name__ == "__main__":
    files = open("walaa.txt", "r")
    content = files.read()
    year = "2024"
    print(ind_upcoming_events(content, year))
