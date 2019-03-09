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

        location_on_disk = "./data/unsafe.csv"
        try:
            Path(location_on_disk).resolve(strict=True)
        except FileNotFoundError:
            infile = "http://data.phishtank.com/data/online-valid.csv"
            df = pd.read_csv(infile)
            df = df[df['verified'] == 'yes']
            df = df[df['online'] == 'yes']
            df['url'].to_csv(location_on_disk, sep=',', encoding='utf-8', header=False,
                             index=False)
        else:
            df = pd.read_csv(location_on_disk)
        self.data["unsafe"] = df.iloc[:,0].values


    def _get_top_1_million(self):
        print("Retrieve top 1 million websites database")
        location_on_disk = "./data/top-1m.csv"
        try:
            Path(location_on_disk).resolve(strict=True)
        except FileNotFoundError:
            distant_file = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
            df = pd.read_csv(infile, compression='zip', header=None)
        else:
            df = pd.read_csv(location_on_disk, header=None)

        self.data["top-1m"] = dict(map(reversed, dict(df.values).items()))
        df.to_csv(location_on_disk, sep=',', encoding='utf-8', index=False)
