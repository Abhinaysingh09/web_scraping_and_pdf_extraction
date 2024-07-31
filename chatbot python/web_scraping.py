from bs4 import BeautifulSoup
import requests
import json

def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

webpages = {
    "about": "https://nbccindia.in/webEnglish/overview",
    "services": "https://nbccindia.in/webEnglish/overview"
}

webpage_data = {}
for key, url in webpages.items():
    webpage_data[key] = scrape_webpage(url)

save_to_json(webpage_data, "webpage_data.json")
