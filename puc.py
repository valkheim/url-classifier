#!/usr/bin/env python
from features import *
from data import *
from features import is_ascii

if __name__ == "__main__":
    p = processor.Processor(n=1337)
    v = visualizer.Visualizer()

#    df = p.get_df()
#    v.scatter_matrix_sns(df)
#
#    X_sm, y_sm = p.prepare_for_scatter_matrix()
#    v.scatter_matrix(X_sm, y_sm)
#
#    df_cm = p.prepare_for_correlation_matrix()
#    v.correlation_matrix(df_cm)

    X_clf, y_clf = p.prepare_for_classifiers()
    v.compare_classifiers_text_para(X_clf, y_clf)

    print("Done.")
