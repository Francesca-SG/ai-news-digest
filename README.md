# AI-Driven News Digest 
 An AI-powered news digest using live feeds from trusted news sources.

### About this project
This is a small web application that gathers news from RSS feeds, scrapes the articles, and sends the text to an AI model to generate a short news summary. User selects a region and topic, and the backend fetches the feeds, parses the XML, gets the article text then AI turns it into a simple summary. I used AI and common online resources whenever I hit concepts I was unfamiliar with. 

### Tech Stack
- Python (Flask, BeautifulSoup, requests, xml.etree)
- Groq API
- JavaScript and HTML for frontend

### How it works
- **Feeds:** Holds a dictionary of RSS URLS grouped by region and topic.
- **Fetch RSS:** Takes those RSS urls, downloads the XML, and pulls article metadata. I currently pull more metadata than I use because I have other features in mind.
- **Summarise:** Uses each article's URL to scrape the webpage, extract the text and combine pieces of each article. 
- **App:** Ties everything together. Gets the feeds, fetches the articles, scrapes them and prepares the text for summarisation.
- **Flask Server + Frontend:** A simple API endpoint and minimal HTML/JavaScript that let's users select a region/topic and generate the digest.

### Skills Demonstrated
- Strengthened my understanding of OOP to break project into small, focused classes, each with one specific task.
- Working with core data structures like lists and dictionaries, moving data cleanly through the pipeline.
- Applied basic algorythmic patterns including iteration and aggregation. Turning RSS data into usable text.
- Intergrated an AI model into a pipeline.
- Tied everything together into a full-stack setup. 

### Future plans
I want to deploy this app to a proper website, improve the codebase, make better use of the metadata I'm currently collecting, and extend the range of regions and topics to generate richer digests. As the project grows, these changes will help reinforce my understanding of OOP and give me more experience with deploying and maintaining a small web application. 
