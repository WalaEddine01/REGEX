#!/bin/python3
"""
Finding books published after 2022
"""
import re
import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('BOOK.xml')
    root = tree.getroot()

    for book in root.findall('book'):
        date = book.find('published').text
        pattrn = "202[2-9]"
        if re.search(pattrn, str(date)):
            print(book.find('title').text)

if __name__ == '__main__':
    main()