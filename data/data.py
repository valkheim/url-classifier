import zipfile, urllib.request, shutil
import pandas as pd
from pathlib import Path


class Data:

    _default_options = {"unsafe": True,
                       "safe": True,
                       "top-1m": True,
                       "tld-stats": True}

    def __init__(self, options=None):
        print("Init Data class")
        if options is None:
            options = self._default_options
        self._data = {}
        self._get_raw_datasets(options)

    def get_data(self):
        return self._data

    def _get_raw_datasets(self, options):
        if options["unsafe"] or options["safe"]: self._get_urls()
        if options["unsafe"]: self._get_unsafe_urls()
        if options["top-1m"]: self._get_safe_urls_top_1_million()
        if options["safe"]: self._get_safe_urls()
        if options["tld-stats"]: self._get_tld_stats()

    def _get_tld_stats(self):
        print("Retrieve tld stats database")

        # remote https://w3techs.com/technologies/overview/top_level_domain/all
        local = "./data/tld-stats.csv"
        try:
            Path(local).resolve(strict=True)
            df = pd.read_csv(local, header=None)
            self._data["tld-stats"] = dict(df.values)
        except FileNotFoundError:
            print("Cannot find", local)

    def _get_unsafe_urls_phishtank(self):
        remote = "http://data.phishtank.com/data/online-valid.csv"
        print("[UNSAFE] Retrive PhishTank database")
        df = pd.read_csv(remote)
        df = df[df['verified'] == 'yes']
        df = df[df['online'] == 'yes']
        return df.iloc[:, 1]

    def _get_unsafe_urls_cybercrime(self):
        print("[UNSAFE] Retrive CyberCrime database")
        remote = "http://cybercrime-tracker.net/all.php"
        return pd.read_csv(remote, header=None)

    def _get_unsafe_urls_unb(self):
        print("[UNSAFE] Retrive University of New Brunswick Canadian Institute for Cybersecurity database")
        local = "./data/FinalDataset/URL/phishing_dataset.csv"
        return pd.read_csv(local, header=None)

    def _get_unsafe_urls(self):
        print("[UNSAFE] Retrieve unsafe urls database")

        local = "./data/unsafe.csv"
        try:
            Path(local).resolve(strict=True)
        except FileNotFoundError:
            df = self._get_unsafe_urls_phishtank()
            df = df.append(self._get_unsafe_urls_cybercrime(), ignore_index=True)
            df = df.append(self._get_unsafe_urls_unb(), ignore_index=True)
            df.to_csv(local, sep=',', encoding='utf-8', header=None, index=False)
        else:
            df = pd.read_csv(local)
        self._data["unsafe"] = df

    def _get_urls(self):
        print("[SAFE|UNSAFE] Retrieve safe/unsafe urls database")

        local = "./data/ISCXURL2016.zip"
        try:
            Path(local).resolve(strict=True)
        except FileNotFoundError:
            remote = "https://iscxdownloads.cs.unb.ca/iscxdownloads/ISCX-URL-2016/ISCXURL2016.zip"
            with urllib.request.urlopen(remote) as response, open(local, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                with zipfile.ZipFile(local) as zf:
                    zf.extractall("./data")

    def _get_safe_urls_top_1_million(self):
        print("[SAFE] Retrieve top 1 million websites database")
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
        return df

    def _get_safe_urls_unb(self):
        print("[SAFE] Retrive University of New Brunswick Canadian Institute for Cybersecurity database")
        local = "./data/FinalDataset/URL/Benign_list_big_final.csv"
        return pd.read_csv(local, header=None)

    def _get_safe_urls(self):
        print("[SAFE] Retrieve safe urls database")

        local = "./data/safe.csv"
        try:
            Path(local).resolve(strict=True)
        except FileNotFoundError:
            df = self._get_safe_urls_top_1_million()
            df = df.iloc[:, 1]
            df = df.append(self._get_safe_urls_unb(), ignore_index=True)
            df.to_csv(local, sep=',', encoding='utf-8', header=None, index=False)
        else:
            df = pd.read_csv(local)
        self._data["safe"] = df
