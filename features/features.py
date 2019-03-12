import features as f

class Features:

    def __init__(self, url=None):
        self._url = url

    def get(self, label, data):
        return [label,
                f.length.get(self._url),
                f.daysSinceRegistration.get(self._url),
                f.tld.get(self._url),
                f.tld_stats.get(self._url, data),
                f.subdomains.get(self._url)]

    @staticmethod
    def get_header():
        return ['label',
                'length',
                'days_since_registration',
                'russian_tld',
                'tld_usage',
                'subdomains']
