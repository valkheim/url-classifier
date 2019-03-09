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

        infile = "http://data.phishtank.com/data/online-valid.csv"
        outfile = "./data/unsafe.csv"

        df = pd.read_csv(infile)
        df = df[df['verified'] == 'yes']
        df = df[df['online'] == 'yes']
        df['url'].to_csv(outfile, sep=',', encoding='utf-8', header=False,
                         index=False)

    def _get_top_1_million(self):
        print("Retrieve top 1 million websites database")

        infile = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
        outfile = "./data/top-1m.csv"

        df = pd.read_csv(infile, compression='zip', header=None)
        self.data["top-1m"] = dict(map(reversed, dict(df.values).items()))
        df.to_csv(outfile, sep=',', encoding='utf-8', index=False)
