#!/usr/bin/env python
import whois
import datetime


def get(address):
    if address is None:
        return None
    try:
        creation = whois.whois(address).creation_date
    except BaseException: # non existent domain raises an exception
        return None
    if creation is None:
        return None
    today = datetime.date.today()
    diff = today - creation.date()
    return diff.days
