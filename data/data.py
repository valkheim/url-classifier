from pathlib import Path
import pandas as pd


class Data:
    data = {}

    def __init__(self):
        print("Init Data class")
        self._get_raw_datasets()

    def _get_raw_datasets(self):
        self._get_unsafe_urls()
        self._get_top_1_million()

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
        self.data["unsafe"] = df.iloc[:, 0].values

    def _get_top_1_million(self):
        print("Retrieve top 1 million websites database")
        local = "./data/top-1m.csv"
        try:
            Path(local).resolve(strict=True)
        except FileNotFoundError:
            remote = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
            df = pd.read_csv(remote, compression='zip', header=None)
        else:
            df = pd.read_csv(local, header=None)

        self.data["top-1m"] = dict(map(reversed, dict(df.values).items()))
        df.to_csv(local, sep=',', encoding='utf-8', index=False)
