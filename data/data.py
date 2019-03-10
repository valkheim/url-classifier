from pathlib import Path
import pandas as pd


class Data:

    _default_options = {"unsafe": True,
                       "safe": True,
                       "top-1m": True}

    def __init__(self, options):
        print("Init Data class")
        if options is None:
            options = self._default_options
        self._data = {}
        self._get_raw_datasets(options)

    def get_data(self):
        return self._data

    def _get_raw_datasets(self, options):
        if options["unsafe"]: self._get_unsafe_urls()
        if options["top-1m"]: self._get_top_1_million()
        if options["safe"]: self._get_safe_urls()

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
        try:
            self._data["safe"] = list(self._data["top-1m"].keys())
            print("Retrieve safe urls database")
        except KeyError as e:
            print("Cannot retrive safe urls database")
            if str(e) == "'top-1m'":
                print("Downloading top-1m dependancy and retry")
                self._get_top_1_million()
                self._get_safe_urls()

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
