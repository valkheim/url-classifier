import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from data import data
from features import features

class Processor(data.Data):

    def __init__(self, fname=None, options=None):
        print("Init Processor class")
        data.Data.__init__(self, options)
        if fname is not None:
            self._load_dataset(fname)
        else:
            self._generate_dataset(100)
            self._save_dataset()

    def _load_dataset(self, fname):
        print("Load dataset",fname)
        self._df = pd.read_csv(fname)

    def _generate_dataset(self, size):
        #preprocess, sanitize, handle features.get() errors
        """
            iterate through safe/unsafe lists of length 'size'
            calculate features scores
            add new row to dataset, eg:
            [0, 16, 432]
             |   |   |
             |   |   +-- days since registration
             |   +-- url length
             +-- label (0: safe, 1: unsafe)
        """
        dataset = []
        unsafe = self.get_data()["unsafe"]
        safe = self.get_data()["safe"]
        balance = unsafe.size if len(safe) > unsafe.size else len(safe)
        balance = size if balance > size else balance
        print("Generate url dataset of size 2 *", balance)
        for url in unsafe[:balance]:
            fn = features.Features(url)
            dataset.append(fn.get(1))
        for url in safe[:balance]:
            fn = features.Features(url)
            dataset.append(fn.get(0))
        self._df = pd.DataFrame(dataset, columns=features.Features().get_header())

    def _save_dataset(self):
        print("Save url dataset")
        path = "./data/dataset.csv"
        self._df.to_csv(path, sep=',', encoding='utf-8', header=True, index=False)

    def _preprocess(self, X, y):
        # Remove variable colineraity
        # rng = np.random.RandomState(2)
        # X += 2 * rng.uniform(size=X.shape)
        X = StandardScaler().fit_transform(X)
        return X, y

    def get(self):
        header = features.Features().get_header()
        X = self._df[header[1::]].to_numpy().astype(float)
        y = self._df[header[0]].to_numpy().astype(float)
        return self._preprocess(X, y)
