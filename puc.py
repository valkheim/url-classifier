#!/usr/bin/env python
from features import *
from data import *
from features import top1m

if __name__ == "__main__":
    p = processor.Processor()
    X, y = p.get()
    v = visualizer.Visualizer()
    #v.scatter_matrix("./data/dataset.csv")
    #v.compare_classifiers(X, y)
    #d = p.get_data()
    #print(top1m.get("http://google.com", d))
