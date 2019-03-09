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
            self._generate_dataset()
        self._save_dataset()

        #next implems
        #self._save_dataset() # write dataset to csv
        #self._load_dataset() # load past dataset

    def _generate_dataset(self):
        print("Generate url dataset")
        """
            iterate through safe/unsafe lists
            calculate features scores
            add new row to dataset, eg:
            [0, 16, 432]
             |   |   |
             |   |   +-- days since registration
             |   +-- url length
             +-- label (0: safe, 1: unsafe)
        """
        dataset = []
        for url in self.get_data()["unsafe"][:100]:
            fn = features.Features(url)
            dataset.append(fn.get(1))
        for url in self.get_data()["safe"][:100]:
            fn = features.Features(url)
            dataset.append(fn.get(0))
        self._df = pd.DataFrame(dataset, columns=features.Features().get_header())

    def _save_dataset(self):
        print("Save url dataset")
        path = "./data/dataset.csv"
        self._df.to_csv(path, sep=',', encoding='utf-8', header=True, index=False)
