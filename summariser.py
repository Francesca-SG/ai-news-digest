# takes articles list, fetches text from link, sends that to AI, returns the digest
import requests
from bs4 import BeautifulSoup as bs
import os
from groq import Groq


class Summarise:

    def get_article(self, url):
        try:
            response = requests.get(url, timeout=10)
            soup = bs(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            return "\n".join(p.get_text() for p in paragraphs)
        except Exception as e:
            print("SCRAPE ERROR:", url, e)
            return ""

    
    def summarise(self, articles):
        # loop through articles, call get_article, combine text, send to AI
        articleText = ""
        for article in articles:
            url = article["link"]
            text = self.get_article(url)
            articleText += text[:350]
        return articleText
    
    def generate_digest(self, articleText, region, topic):

        client = Groq(
            api_key = os.environ.get("GROQ_API_KEY")
        )

        prompt = (
            f"Summarise the following news articles into a digest for general audiences. "
            f"Keep it concise, structured, and reference the news outlets. "
            f"Summary should be no more than around 150 words. "
            f"Begin immediately with the news content, no introductions or meta-commentary. "
            f"If no news articles are provided, do not provide any output. "
            f"Region: {region}. Topic: {topic}.\n\n"
            f"{articleText}"
        )

        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile"
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print("GROQ ERROR:", e)
            return "AI summarisation failed."

