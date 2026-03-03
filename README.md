# AI-Driven News Digest 
AI-powered news digest using live feeds.
This tool uses AI to create news summaries using RSS feeds from trusted news sources.

### About this project
This is a small web application that gathers news from RSS feeds, scrapes the articles, and sends the text to an AI model to generate a short news summary. User selects a region and topic, and the backend fetches the feeds, parses the XML, gets the article text then AI turns it into a simple summary. 

### How it works
**Feeds:** Holds a dictionary of RSS URLS grouped by region and topic.
**Fetch RSS:** Takes those RSS urls, downloads the XML, and pulls article metadata. I currently pull more metadata than I use because I have other features in mind.
**Summarise:** Uses each article's URL to scrape the webpage, extract the text and combine pieces of each article. 
**App:** Ties everything together. Gets the feeds, fetches the articles, scrapes them and prepares the text for summarisation.
**Flask Server + Frontend:** A simple API endpoint and minimal HTML/JavaScript that let's users select a region/topic and generate the digest.

###
