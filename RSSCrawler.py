import feedparser


class RSSCrawler:

    # Internal variable and feed query param map
    FEED_KEY_PARAMS = {"name": "cond", "count": "count", "days": "rcv_d"}

    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def call_feed(url: str) -> dict:
        """Fetches RSS feed from url

        :returns
        dict -- RSS Feed

        :argument
        url: str -- url to invoke
        """

        if not url:
            return {}
        feed = feedparser.parse(url)
        return feed

    def generate_url(self, param: dict) -> str:
        """Generates full url with params

        :returns
        str -- complete url with query param

        :argument
        param: dict -- parameters as dictionary to be converted to url query param
        """

        if not param:
            return self.base_url

        query_params = []  # making it as list as string is immutable, may cause performance degradation
        for key in param:
            if not param[key]:
                continue
            words = str(param[key]).split()
            print(words)
            query_params.append(f"{key}={'+'.join(words)}")
        return self.base_url + "?" + "&".join(query_params)

    def get_feed(self, name: str, day_num: int, count: int = 10) -> dict:
        """Return feed

        :returns
        dict -- RSS Feed

        :argument
        name: str -- name of disease
        day_num: int -- number of results
        count: int -- number of results (default 10)
        """

        params = {RSSCrawler.FEED_KEY_PARAMS["name"]: name, RSSCrawler.FEED_KEY_PARAMS["days"]: str(day_num),
                  "count": str(count)}
        url = self.generate_url(params)
        print(url)
        return RSSCrawler.call_feed(url)

    def was_active_in_days(self, disease_name: str, day_num: int):
        return len(self.get_feed(disease_name, day_num, 1)['entries']) > 0


if __name__ == "__main__":
    crawler = RSSCrawler("https://clinicaltrials.gov/ct2/results/rss.xml")
    ans = crawler.was_active_in_days("Alzheimer Disease", 140)
    print(ans)
