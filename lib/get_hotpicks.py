import requests
from bs4 import BeautifulSoup
import datetime
from rfeed import Item, Feed

def get_hotpicks(url: str):
    response = requests.get(url)
    site = BeautifulSoup(response.content, 'html.parser')
    hot_picks = site.findAll('div', attrs={'class': 'hotpicks'})
    movies = []
    for item in hot_picks:
        link = f"https://torrentgalaxy.to{item.find('a').get('href')}"
        poster = item.find('img').get('data-src')
        name = item.find('img').get('alt')
        if poster:
            movies.append({"link": link, "poster": poster, "name": name})
    return movies

def get_feed(movies: list):
    items = []
    for movie in movies:
        item = Item(
            title = movie.get('name'),
            link = movie.get('link'),
            description = "Movies-HD",
            #category = "Movies : HD",
            comments = f"{movie.get('link')}/{movie.get('name')}"
            )
        items.append(item)
    

    feed = Feed(
        title = "TorrentGalaxy",
        link = "https://torrentgalaxy.to",
        description = "TorrentGalaxy RSS Feed",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = items
        )
    return feed.rss()