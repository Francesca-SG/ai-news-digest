#For RSS URLs, fetch the XML and turn it into article data.
import requests 
import xml.etree.ElementTree as ET

class FetchRSS:
    def fetch(self, url):
        articles = []
        # get url
        # return xml text
        # try, except
        try:
            element = requests.get(url)
            #read xml.url
            element = element.text 
            tree = ET.fromstring(element)
            channel = tree.find("channel")
            items = channel.findall("item")

            for item in items:
                title = item.find("title")
                link = item.find("link")
                desc = item.find("description")
                pub_date = item.find("pubDate")

                article = {
                    "title": title.text,
                    "link": link.text,
                    "desc": desc.text,
                    "pub_date": pub_date.text
                }
                articles.append(article)
                
            return articles
        
        except Exception as e:
            print("RSS Error", url, e)
            return []