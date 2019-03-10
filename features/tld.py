#!/usr/bin/env python
import tldextract

# Russian tld ?
def get(address):
    return 1 if tldextract.extract(address) == "ru" else 0
