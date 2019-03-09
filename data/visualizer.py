import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from matplotlib import cm
from features import features

class Visualizer:
    def __init__(self):
        print("Init Visualizer class")

    def scatter_matrix(self,fname):
        header = features.Features().get_header()
        df = pd.read_csv(fname)
        X = df[header[1::]]
        y = df[header[0]]
        cmap = cm.get_cmap('bwr')
        scatter_matrix(X, c=y, marker='o', figsize=(9,9), cmap=cmap)
        plt.suptitle('Scatter-matrix for each input feature')
        plt.savefig('./views/scatter_matrix_for_dataset.png')
