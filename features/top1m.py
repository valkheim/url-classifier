#!/usr/bin/env python
import csv
from urllib.parse import urlparse


def getHostname(address):
    url = urlparse(address)
    if url.hostname is not None:
        return url.hostname
    else:
        raise ValueError(address)


def get(address, data):
    try:
        hostname = getHostname(address)
        ret = data["top-1m"][hostname]
        print("Got rank", ret, "for", hostname)
        return ret
    except KeyError as e:
        print("Unknow rank for", e)
        return 0
    except ValueError as e:
        print("Bad value for", e)
        return 0
    except BaseException:
        print("Unknow exception, reraise")
        raise
