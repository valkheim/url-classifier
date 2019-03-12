#!/usr/bin/env python
from features import *
from data import *
from features import top1m

if __name__ == "__main__":
    fname = "./data/dataset.csv"
    #p = processor.Processor(fname=fname)
    p = processor.Processor(n=10)
    df = p.get_df()
    v = visualizer.Visualizer()
    #v.scatter_matrix(fname)
    v.correlation_matrix(df)
    #v.scatter_matrix_seaborn(df)
    #v.compare_classifiers(X, y) # 2 dimensions graph, only 2 features
    #v.compare_classifiers_text_para(X, y)
    print("Done.")
