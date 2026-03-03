# Dictionary of RSS feeds
class Feeds:

    # Constructor method
    def __init__(self):
        self.feeds = {
            "World": {
                "Politics": [
                    "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
                ],
                "Technology": [
                    
                    "https://www.theguardian.com/uk/technology/rss",
                    "https://feeds.npr.org/1019/rss.xml"
                ],
                "World": [
                    
                    "https://www.theguardian.com/world/rss",
                    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
                ],
            },
            "US": {
                "Politics": [
                    "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
                ],
                "Technology": [
                    
                    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
                ],
                "World": [
                    
                    "https://www.theguardian.com/world/rss",
                    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
                ]
            }
        }
        
    def getURL(self, region, category):
        return self.feeds[region][category]
    

    