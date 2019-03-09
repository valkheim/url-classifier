#!/usr/bin/env python
from features import *
from data import *
from features import top1m

if __name__ == "__main__":
    p = processor.Processor()
    v = visualizer.Visualizer()
    v.scatter_matrix("./data/dataset.csv")
    #d = p.get_data()
    #print(top1m.get("http://google.com", d))
