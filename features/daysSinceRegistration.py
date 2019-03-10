#!/usr/bin/env python
import whois
import datetime
import numpy as np


def get(address):
    if address is None:
        return np.nan
    try:
        creation = whois.whois(address).creation_date
    except BaseException:  # non existent domain raises an exception
        return np.nan
    if creation is None:
        return np.nan
    today = datetime.date.today()
    try:
        if type(creation) == list:
            diff = today - creation[-1].date()
        else:
            diff = today - creation.date()
    except BaseException: #AttributeError for amazon.co.uk : before Aug-1996
        return np.nan

    return diff.days
