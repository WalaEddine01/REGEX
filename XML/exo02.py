#!/bin/python3
"""
Pretty print XML with added elements
"""

import xml.etree.ElementTree as ET

def addElements(r):
    """
    Add elements to the XML tree
    """
    new_book = ET.SubElement(r, "book")
    new_book.attrib = {"id": "105"}
    
    title = ET.SubElement(new_book, "title")
    title.text = "Data Science Fundamentals"
    
    author = ET.SubElement(new_book, "author")
    author.text = "Linda Green"
    
    genre = ET.SubElement(new_book, "genre")
    genre.text = "Data Science"
    
    price = ET.SubElement(new_book, "price")
    price.text = "40.99 USD"
    
    published = ET.SubElement(new_book, "published")
    published.text = "2023-11-20"
    
    rating = ET.SubElement(new_book, "rating")
    rating.text = "4.9"

def prettyPrintXml(r):
    """
    Pretty prnt XML
    """
    ET.indent(r, space="\t")
    return ET.tostring(r, encoding='utf-8').decode()


if __name__ == "__main__":
    t = ET.parse('BOOK.xml')
    r = t.getroot()

    addElements(r)

    prettyXml = prettyPrintXml(r)

    with open("BOOK.xml", "w") as f:
        f.write(prettyXml)