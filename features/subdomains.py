#!/usr/bin/env python
from urllib.parse import urlparse


def get(address):
    url = urlparse(address)
    if (url.hostname is not None):
        subdomains = url.hostname.split('.')
        return len(subdomains) - 2
    return 0
