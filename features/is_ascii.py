#!/usr/bin/env python

def get(address):
    try:
        address.encode('ascii')
    except UnicodeEncodeError:
        return 1
    else:
        return 0
