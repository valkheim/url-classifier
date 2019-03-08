#!/usr/bin/env python
from urllib.parse import urlparse


def get(address):
    url = urlparse(address)
    if url.hostname is not None:
        tld = url.hostname.split('.')[-1]
        return tld
