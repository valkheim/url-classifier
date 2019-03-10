#!/usr/bin/env python
from features import *
from data import *
from features import top1m

if __name__ == "__main__":
    fname = "./data/dataset.csv"
    #p = processor.Processor(fname=fname)
    p = processor.Processor()
    X, y = p.get()
    print(X.shape)
    print(X)
    print(y.shape)
    print(y)
    v = visualizer.Visualizer()
    v.scatter_matrix("./data/dataset.csv")
    #v.compare_classifiers(X, y) # 2 dimensions, 2 features
    print("Done.")
