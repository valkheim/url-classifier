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


class Visualizer:
    def __init__(self):
        print("Init Visualizer class")

    def scatter_matrix(self, fname):
        try:
            header = features.Features().get_header()
            df = pd.read_csv(fname)
            df = df + 0.00001 * np.random.rand(df.shape[0], df.shape[1]) # remove singularity
            X = df[header[1::]]
            y = df[header[0]]
            cmap = cm.get_cmap('bwr')
            scatter_matrix(X, c=y, marker='o', figsize=(9,9), cmap=cmap, diagonal='kde')
            plt.suptitle('Scatter-matrix for each input feature')
            plt.savefig('./views/scatter_matrix_for_dataset.png')
        except BaseException as e: # might trigger an singular matrix with many simulations
            print("scatter matrix generation failed somewhere", e)

    def correlation_matrix(self, df, size=10):
        sns.set(style="white")

        # Compute the correlation matrix on features
        df.drop('label', axis=1, inplace=True)
        corr = df.corr()
        print("Correlation matrix on features")
        print(corr.to_string())

        # Generate a mask for the upper triangle
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

        f, ax = plt.subplots(figsize=(11, 9))

        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        sns_plot = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})

        sns_plot.set_title("Correlation matrix for each input (triangle shape)")
        figure = sns_plot.get_figure()
        figure.savefig('./views/correlation_matrix_for_dataset.png')



    def compare_classifiers(self, X, y):
        """
            https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
            transparent plots : testing plots
            non-transparent plots : training plots
        """
        plot_index = 1

        names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
                 "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
                 "Naive Bayes", "QDA"]

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
            QuadraticDiscriminantAnalysis()]

        plt.figure(figsize=(20, 3))

        X_train, X_test, y_train, y_test = \
            train_test_split(X, y, test_size=.4, random_state=42)

        x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
        y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                             np.arange(y_min, y_max, .02))

        # Plot dataset
        cm = plt.cm.RdBu
        cm_bright = ListedColormap(['#FF0000', '#0000FF'])
        ax = plt.subplot(1, len(classifiers) + 1, plot_index)
        plot_index += 1
        ax.set_title("Input data")
        # Plot training points
        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                   edgecolors='k')
        # Plot testing points
        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=.5,
                   edgecolors='k')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())

        # Iterate over classifiers
        for name, clf in zip(names, classifiers):
            ax = plt.subplot(1, len(classifiers) + 1, plot_index)
            clf.fit(X_train, y_train)
            score = clf.score(X_test, y_test)
            table.append_row([name, score])

            # Plot the decision boundary. For that, we will assign a color to each
            # point in the mesh [x_min, x_max]x[y_min, y_max].
            # https://stackoverflow.com/questions/29948156/scitkit-learn-query-data-dimension-must-match-training-data-dimension?rq=1
            if hasattr(clf, "decision_function"):
                Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
            else:
                Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
            # Put the result into a color plot
            Z = Z.reshape(xx.shape)
            ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)

            # Plot training points
            ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                       edgecolors='k')
            # Plot testing points
            ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
                       edgecolors='k', alpha=.5)

            ax.set_xlim(xx.min(), xx.max())
            ax.set_ylim(yy.min(), yy.max())
            ax.set_xticks(())
            ax.set_yticks(())
            ax.set_title(name)
            ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
                    size=15, horizontalalignment='right')
            plot_index += 1

        plt.suptitle('Classifiers comparison')
        plt.tight_layout(rect=[0, 0.03, 1, 0.9])
        plt.savefig('./views/classifiers-comparison.png')

    def compare_classifiers_text(self, X, y):
        names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
                 "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
                 "Naive Bayes", "Linear discriminant analysis", "QDA"]

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

        table = BeautifulTable()
        table.column_headers = ["name", "score"]
        total = 0
        for name, clf in zip(names, classifiers):
            clf.fit(X_train, y_train)
            # score is a shortcut to predict/calculate accuracy
            score = clf.score(X_test, y_test)
            table.append_row([name, score])
            total += score

        # print score by classifier table
        total /= len(classifiers)
        table.append_row(["Total", score])
        print(table)

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
