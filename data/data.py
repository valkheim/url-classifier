from pathlib import Path
import pandas as pd


class Data:

    # give what to init as paramter
    def __init__(self):
        print("Init Data class")
        self._data = {}
        self._get_raw_datasets()

    def get_data(self):
        return self._data

    def _get_raw_datasets(self):
        self._get_unsafe_urls()
        self._get_top_1_million()
        self._get_safe_urls()

    def _get_unsafe_urls(self):
        print("Retrieve unsafe urls database")

        local = "./data/unsafe.csv"
        try:
            Path(local).resolve(strict=True)
        except FileNotFoundError:
            remote = "http://data.phishtank.com/data/online-valid.csv"
            df = pd.read_csv(infile)
            df = df[df['verified'] == 'yes']
            df = df[df['online'] == 'yes']
            df['url'].to_csv(remote, sep=',', encoding='utf-8',
                             header=False, index=False)
        else:
            df = pd.read_csv(local)
        self._data["unsafe"] = df.iloc[:, 0].values

    def _get_safe_urls(self):
        print("Retrieve safe urls database")
        self._data["safe"] = list(self._data["top-1m"].keys())

    def _get_top_1_million(self):
        print("Retrieve top 1 million websites database")
        local = "./data/top-1m.csv"
        try:
            Path(local).resolve(strict=True)
        except FileNotFoundError:
            remote = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
            df = pd.read_csv(remote, compression='zip', header=None)
            df.to_csv(local, sep=',', encoding='utf-8', header=None, index=False)
        else:
            df = pd.read_csv(local, header=None)

        self._data["top-1m"] = dict(map(reversed, dict(df.values).items()))
