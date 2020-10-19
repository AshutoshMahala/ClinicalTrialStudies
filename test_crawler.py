from RSSCrawler import RSSCrawler


# To test instance
class TestInstance:

    # Test to instantiate
    def test_instance(self):
        crawler = RSSCrawler("https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d=1200&lup_d=&sel_rss=new14&cond=Wolman+Disease&count=10000")
        assert True


# To test call_feed
class TestCallFeed:

    # Test to call actual url
    def test_call_feed(self):
        feed = RSSCrawler.call_feed("https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d=1200&lup_d=&sel_rss=new14&cond=Wolman+Disease&count=10000")
        assert feed

    # Test to handle None
    def test_call_feed_none(self):
        feed = RSSCrawler.call_feed(None)
        assert len(feed) == 0

    # Test to handle empty string
    def test_call_feed_empty(self):
        feed = RSSCrawler.call_feed("")
        assert len(feed) == 0


# To test get_feed
class TestGetFeed:

    # Test to get feeds
    def test_get_actual_feed(self):
        crawler = RSSCrawler("https://clinicaltrials.gov/ct2/results/rss.xml")
        feed = crawler.get_feed("Alzheimer Disease", 140, 10)
        assert len(feed['entries']) == 10

    # Test to get feed less than 1
    def test_get_feed_invalid_days(self):
        crawler = RSSCrawler("https://clinicaltrials.gov/ct2/results/rss.xml")
        feed = crawler.get_feed("Wolman Disease", -1, 10)
        assert len(feed['entries']) == 0

    # Test to get feed less than 1
    def test_get_feed_invalid_count(self):
        crawler = RSSCrawler("https://clinicaltrials.gov/ct2/results/rss.xml")
        feed = crawler.get_feed("Wolman Disease", 100, -10)
        assert len(feed['entries']) == 1

    # Test to get feed less than 1
    def test_get_feed_invalid_name(self):
        crawler = RSSCrawler("https://clinicaltrials.gov/ct2/results/rss.xml")
        feed = crawler.get_feed("Wolmanrr Disease", 100, 10)
        assert len(feed['entries']) == 0


class TestGenerateUrl:

    # Test to generate query param with correct strings
    def test_generate_url_correct(self):
        crawler = RSSCrawler("abcd.com")
        uri = crawler.generate_url({"a": "b", "c": "d e"})
        assert uri == "abcd.com?a=b&c=d+e"

    # Test to generate query param with int
    def test_generate_url_with_int_parse(self):
        crawler = RSSCrawler("abcd.com")
        uri = crawler.generate_url({"a": 1, "c": "d e"})
        assert uri == "abcd.com?a=1&c=d+e"

    # Test to generate query param with None
    def test_generate_url_with_None(self):
        crawler = RSSCrawler("abcd.com")
        uri = crawler.generate_url({"a": None, "c": "d e"})
        assert uri == "abcd.com?c=d+e"

    # Test to generate query param with None
    def test_generate_url_empty_param(self):
        crawler = RSSCrawler("abcd.com")
        uri = crawler.generate_url({})
        assert uri == "abcd.com"

    # Test to generate query param with None
    def test_generate_url_None_param(self):
        crawler = RSSCrawler("abcd.com")
        uri = crawler.generate_url(None)
        assert uri == "abcd.com"
