import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
from pandas.plotting import scatter_matrix
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from features import features
from beautifultable import BeautifulTable
from multiprocessing import Process, Manager
from data import processor


class Visualizer:

    def __init__(self):
        print("Init Visualizer class")

    def scatter_matrix_sns(self, df):
        import seaborn as sns
        sns.set(style="ticks")

        #df = sns.load_dataset("iris")
        sns.pairplot(df, hue="label")
        figure = sns_plot.get_figure()
        figure.savefig('out.png')

    def scatter_matrix(self, X, y):
        cmap = cm.get_cmap('bwr')
        scatter_matrix(X, c=y, marker='o', figsize=(9,9), cmap=cmap,
                       diagonal='kde')
        plt.suptitle('Scatter-matrix for each input feature')
        plt.savefig('./views/scatter_matrix_for_dataset.png')


    def correlation_matrix(self, df, size=10):
        sns.set(style="white")
        corr = df.corr()
        title = " Correlation matrix for each feature "
        print("-" * 5 + title + "-" * (70 - len(title)))
        print(corr.to_string())
        print("-" * 75)
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        f, ax = plt.subplots(figsize=(11, 9))
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns_plot = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                               square=True, linewidths=.5,
                               cbar_kws={"shrink": .5})
        sns_plot.set_title("Correlation matrix for each input (triangle shape)")
        figure = sns_plot.get_figure()
        figure.savefig('./views/correlation_matrix_for_dataset.png')


    def _compute_clf(self, clf, name, X_train, X_test, y_train, y_test):
        clf.fit(X_train, y_train)
        ## score is a shortcut to predict/calculate accuracy
        score = clf.score(X_test, y_test)
        print(score, "\t", name)


    def compare_classifiers_text_para(self, X, y):

        names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
                 "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
                 "Naive Bayes", "Linear discriminant analysis", "QDA"]

        processes = {}

        classifiers = [
            KNeighborsClassifier(3),
            SVC(kernel="linear", C=0.025),
            SVC(gamma=2, C=1),
            GaussianProcessClassifier(1.0 * RBF(1.0)),
            DecisionTreeClassifier(max_depth=5),
            RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
            MLPClassifier(alpha=1),
            AdaBoostClassifier(),
            GaussianNB(),
            LinearDiscriminantAnalysis(),
            QuadraticDiscriminantAnalysis()]

        X_train, X_test, y_train, y_test = \
            train_test_split(X, y, test_size=.4, random_state=42)

        print("-"*5+" Results "+"-"*(30-len(" Results ")))
        for name, clf in zip(names, classifiers):
            processes[name] = Process(target=self._compute_clf, args=(clf, name, X_train, X_test, y_train, y_test))
            processes[name].start()
        for name, clf in zip(names, classifiers):
            processes[name].join()
        print("-"*35)
