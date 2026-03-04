# 🤖📰 AI-Driven Daily News Digest 
> **An AI-powered news digest using live feeds from trusted news sources.**
***
## 🧭 About this project
This is a small web application that gathers news from RSS feeds, scrapes the articles, and sends the text to an AI model to generate a short news summary. User selects a region and topic, and the backend fetches the feeds, parses the XML, gets the article text then AI turns it into a simple summary. 

***
## 🧰 Tech Stack
- Python (Flask, BeautifulSoup, requests, xml.etree)
- Llama 3.3 (GROQ API)
- JavaScript and HTML for frontend
***
## How it works
- 📰 **Feeds:** Holds a dictionary of RSS URLS grouped by region and topic.
- 🧲 **Fetch RSS:** Takes those RSS urls, downloads the XML, and pulls article metadata. I currently pull more metadata than I use because I have other features in mind.
- 🧠 **Summarise:** Uses each article's URL to scrape the webpage, extract the text and combine pieces of each article. 
- ⚙️ **App:** Ties everything together. Gets the feeds, fetches the articles, scrapes them and prepares the text for summarisation.
- 🌐 **Flask Server + Frontend:** A simple API endpoint and minimal HTML/JavaScript that let's users select a region/topic and generate the digest.
***
## 🧠 Skills Demonstrated
- Strengthened my understanding of OOP to break project into small, focused classes, each with one specific task.
- Working with core data structures like lists and dictionaries, moving data cleanly through the pipeline.
- Applied basic algorythmic patterns including iteration and aggregation. Turning RSS data into usable text.
- Intergrated an AI model into a pipeline.
- Tied everything together into a full-stack setup. 
***
## 🚧 Challenges I worked through
- Finding reliable RSS feeds was difficult, as many major outlets don't provide them, made consistent coverage difficult.
- Accidentally sending far more text than the API allowed. To fix this I limited the generated text from uncapped to 350.
***
## 🚀 Future plans
I want to deploy this app to a proper website, as well as improve the overall look and feel of the site. Additionally, I plan to improve the codebase, make better use of the metadata I'm currently collecting, and extend the range of regions and topics to generate richer digests. As the project grows, these changes will help reinforce my understanding of OOP and give me more experience with deploying and maintaining a small web application. 

The AI occasionally over explains, adding extra details that aren't necessary for the final summary. To address this, I plan to introduce stricter prompt templates and a simple processing layer to clean up any anomalous outputs. There is also a limit on the size of the combined articles that can be sent to the AI for summarisation. As a result, the summary sometimes ends up relying on a single source. I plan to fix this by summarising articles individually and then generating a combined summary. This will ensure multiple sources are represented and reduce single source bias.
***
## 🖼️ Screenshots
Below are images of the application in action. 
<img width="741" height="199" alt="Screenshot 2026-03-04 075515" src="https://github.com/user-attachments/assets/177885ec-eedd-47d0-8c24-77bcd7efdd00" />
<img width="739" height="175" alt="Screenshot 2026-03-04 075634" src="https://github.com/user-attachments/assets/28baa13f-e6e9-4826-a4b6-c68d1c22b177" />
***
### 🗒️ Notes
- To determine the most trusted new sources, I used a you.gov article entitle Trust in Media 2025: Which news sources Americans use and trust. I only considered popular news outlets with a +10 or more.
- I used AI and common online resources whenever I hit concepts I was unfamiliar with. 

