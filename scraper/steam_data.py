import requests
from bs4 import BeautifulSoup

headline = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def famous__games():
    link="https://store.steampowered.com/search/?filter=topsellers"
    response = requests.get(link, headers=headline)
    soup = BeautifulSoup(response.text, "html.parser")
    outputs = []
    videogames = soup.find_all("a", class_="search_result_row")
    skip_keywords = ['steam deck', 'controller', 'bundle']
    for game in videogames[:10]:
        title_t = game.find("span", class_="title")
        link = game.get("href", "#")
        if title_t:
            title = title_t.text.strip()
            if any(word in title.lower() for word in skip_keywords):
                continue
            outputs.append({
                "title": title,
                "link": link
            })
        if len(outputs) >= 10:
            break
    return outputs
