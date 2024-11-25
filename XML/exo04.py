#!/bin/python3
"""
Convert the XML file to a JSON file
"""

import xml.etree.ElementTree as ET
from json import dump

def main():
    """
    """
    tree = ET.parse('BOOK.xml')
    root = tree.getroot()
    
    books = {"books": {}}
    magazines = {"magazines": {}}

    for i in root.findall("book"):        
        books["books"][f"Book with ID {i.attrib['id']}"] = {
            "title": i.find('title').text,
            "author": i.find("author").text,
            "genre": i.find("genre").text,
            "price": i.find("price").text,
            "published": i.find("published").text,
        }
        try:
            books["books"][f"Book with ID {i.attrib['id']}"]["rating"] = i.find("rating").text
        except AttributeError:
            books["books"][f"Book with ID {i.attrib['id']}"]["rating"] = "No rating available"
        
        try:
            books["books"][f"Book with ID {i.attrib['id']}"]["publisher"] = i.find("publisher").text
        except AttributeError:
            books["books"][f"Book with ID {i.attrib['id']}"]["publisher"] = "No publisher available"

    for j in root.findall('magazine'):
        magazines["magazines"][f"Magazine with ID {j.attrib['id']}"] = {
            "title": j.find('title').text,
            "editor": j.find('editor').text,
            "category": j.find('category').text,
            "price": j.find('price').text,
            "published": j.find('published').text,
            "frequency": j.find('frequency').text,
        }

    return books, magazines

if __name__ == '__main__':
    books, magazines = main()
    
    with open("BOOKS.json", "w") as f:
        dump(books, f, indent=4)
    with open("MAGAZINES.json", "w") as f:
        dump(magazines, f, indent=4)
