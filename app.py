from backend.feeds import Feeds
from backend.fetch_rss import FetchRSS  
from backend.summariser import Summarise

class App:

    def run(self, region, topic):
        feeds = Feeds()
        fetch_rss = FetchRSS()
        summarise = Summarise()

        urls = feeds.getURL(region, topic)

        all_articles = []
        for url in urls:
            result = fetch_rss.fetch(url)
            all_articles.extend(result)

        article_text = summarise.summarise(all_articles)
        digest = summarise.generate_digest(article_text, region, topic)
            
        return digest

