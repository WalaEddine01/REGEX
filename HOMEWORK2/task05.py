#!/bin/python3
"""
Extract Hashtags from Social Media Posts 
"""
import re

def extract_hashtags(text):
    """
    This function extracts hashtags from a text.
    """
    pattr = r"#(\w+)"
    res = re.findall(pattr, text)
    return res

if __name__ == "__main__":

    text01 = "I am learning #Python and #DataScience"
    text02 = "I am learning #Python and #DataScience in #2021"
    text03 = "I am learning #Python and #DataScience in #2021 and #2022"
    
    print(extract_hashtags(text01))
    print(extract_hashtags(text02))
    print(extract_hashtags(text03))