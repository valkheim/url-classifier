import pandas as pd
from data import data
from features import features

class Processor(data.Data):

    def __init__(self, dataset_fname=None):
        print("Init Processor class")
        data.Data.__init__(self)
        if dataset_fname:
            print("Load dataset",dataset_fname)
        else:
            self._generate_dataset(100)
        self._save_dataset()

        #next implems
        #preprocess, sanitize, handle features.get() errors
        #self._save_dataset() # write dataset to csv
        #self._load_dataset() # load past dataset

    def _generate_dataset(self, size):
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

    def get(self):
        header = features.Features().get_header()
        X = self._df[header[1::]].to_numpy().astype(float)
        y = self._df[header[0]].to_numpy().astype(float)
        return X, y
