#!/usr/bin/env python
from features import *
from data import data
from features import top1m

if __name__ == "__main__":
    dt = data.Data()
    print(top1m.get("http://google.com", dt.data))
