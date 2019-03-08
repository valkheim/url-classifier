#!/usr/bin/env python
import csv
from urllib.parse import urlparse


runtime = {}
runtime["top-1m"] = None

def tryLoad(fname):
    if runtime["top-1m"] is None:
        print("Load", fname)
        with open(fname, mode='r') as infile:
            reader = csv.reader(infile)
            d = dict((rows[1],rows[0]) for rows in reader)
        runtime["top-1m"] = d
        return d
    return runtime["top-1m"]


def getHostname(address):
    url = urlparse(address)
    if url.hostname is not None:
        return url.hostname
    else:
        raise ValueError(address)


def get(address):
    try:
        hostname = getHostname(address)
        tryLoad("./data/top-1m.csv")
        ret = runtime["top-1m"][hostname]
        print("got rank",ret,"for",hostname)
    except KeyError as e:
        print("Unknow rank for", e)
        return 0;
    except ValueError as e:
        print("Bad value for", e)
        return 0;
    except:
        print("Unknow exception, reraise")
        raise
    return ret
