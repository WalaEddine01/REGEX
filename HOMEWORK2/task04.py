#!/bin/python3
"""
Password Validation
"""
import re

def validate_password(password):
    """
    This function validates a password to make sure it meets the criteria.
    """
    pattr = r"\b([a-z]{1,}|[A-Z]{1,}|[0-9]{1,}|[\W]{1,}){10,}\b"
    res = re.fullmatch(pattr, password)
    return res

if __name__ == "__main__":

    password01 = "Secure!2021"
    password02 = "Research@1234"
    password03 = "Res@1234"
    
    print(validate_password(password01) != None)
    print(validate_password(password02) != None)
    print(validate_password(password03) != None)