#!/usr/bin/python3
# Author - Richard Rossi Adjei

def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
