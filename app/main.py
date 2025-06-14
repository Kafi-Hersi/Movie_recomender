from bs4 import BeautifulSoup
import requests as HTTP
import random
def main(country):
    urls = [
        # 'https://myflixerz.to/filter?type=all&quality=all&release_year=all&genre=all&country=40-109-62'
        f'https://myflixerz.to/country/{country}',
        f'https://myflixerz.to/country/{country}?page=2',
        f'https://myflixerz.to/country/{country}?page=3'
    ]

    movie_titles = []
    movie_ids = []
    for url in urls:
        response = HTTP.get(url)
        
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        # Find all h2 tags with class 'film-name'
        film_headers = soup.find_all('h2', class_='film-name')
        for h2 in film_headers:
            a = h2.find('a')
            if a and a.has_attr('href'):
                href = a['href']
                ids = href.split('/')[-1]
                title = a.text.strip()

                movie_ids.append(ids)
                movie_titles.append(title)
    return movie_ids, movie_titles

def recomend(movie_ids):
    gues = random.randint(0, len(movie_ids) -1)
    return gues
