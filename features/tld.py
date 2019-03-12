#!/usr/bin/env python
import tldextract

# Russian tld ?
def get(address):
    cache_extract = tldextract.TLDExtract(cache_file="./data/tld.cache")
    return 1 if cache_extract(address) == "ru" else 0
