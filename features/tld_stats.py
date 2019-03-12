#!/usr/bin/env python
import tldextract

def get(address, data):
    cache_extract = tldextract.TLDExtract(cache_file="./data/tld.cache")
    tld = cache_extract(address).suffix
    try:
        return data["tld-stats"][tld]
    except BaseException:
        return 0.1

