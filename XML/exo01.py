#!/bin/python3
"""

"""
import xml.etree.ElementTree as ET

def parseXml():
    """
    """
    tree = ET.parse('BOOK.xml')
    root = tree.getroot()
    
    books = {}
    editors = {}

    for i in root.findall("book"):
        books[f"Book with ID {i.attrib['id']}"] = {
            "title": i.find('title').text,
            "author": i.find("author").text
        }

    for j in root.findall('magazine'):
        editors[f"Magazine with ID {j.attrib['id']}"] = {
            "Editor": j.find('editor').text
        }

    return books, editors

if __name__ == '__main__':
    books, editors = parseXml()

    print(books)
    print(editors)