#!/bin/python3
"""
This module extracts emails from a given text.
"""
import re

def extract_emails(text):
    """
    Extracts emails from a given text.
    """
    pattr = r'((?:[a-zA-Z._]+)(?:@|\[at\])(?:[a-zA-Z._%+-\[\]]+)\.(?:[cC][oO][mM]|[cC][oO]\.[uU][kK]))'
    emails = re.findall(pattr, text)
    for email in range(len(emails)):
        for i in range(len(emails[email])):
            if emails[email][i] == "[":
                if emails[email][i+1:i+3] == "at":
                    emails[email] = emails[email][:i] + "@" + emails[email][i+4:]
                    break
    
    print(emails)


if __name__ == "__main__":
    string = "waa@wal.com  wa[at]xd.co.uk waala@[we.b].com"
    extract_emails(string)