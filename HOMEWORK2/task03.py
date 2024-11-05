#!/bin/python3
"""
This module Extract and Transform Dates
"""
import re

def extract_dates(text):
    """
    Extracts dates from text in various formats and returns them in their original format.
    """
    patterns = [
        r'\b(\d{2})/(\d{2})/(\d{4})\b',                                 # DD/MM/YYYY
        r'\b(\d{2})\.(\d{2})\.(\d{4})\b',                               # DD.MM.YYYY
        r'\b(\d{4})/(\d{2})/(\d{2})\b',                                 # YYYY/MM/DD
        r'\b(\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\s+the\s+\d{1,2}(?:st|nd|rd|th)?\s+of\s+(?:January|February|March|April|May|June|July|August|September|October|November|December),?\s+\d{4})\b',
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{4}\b'  # Month DDth, YYYY
    ]

    dates = []
    
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if len(match) == 3:
                dates.append(f"{match[0]}/{match[1]}/{match[2]}")
            else:
                split_date = re.split(r'[\s,]', match)
                for i in split_date:
                    which_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                    if i in which_month:
                        month = which_month.index(i) + 1
                    elif i.isdigit() and len(i) == 4:
                        year = i
                    elif len(i) == 4:
                        day = i[:2]
                dates.append(f"{day}/{month}/{year}")
    return dates

if __name__ == "__main__":
    text = """
    Here are some dates: 15/08/1980, 10.12.2024, 2019/11/29, Friday, the 31st of January, 2025, 
    and April 23rd, 2015.
    """
    
    original_dates = extract_dates(text)
    print(original_dates)