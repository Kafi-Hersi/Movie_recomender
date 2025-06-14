from bs4 import BeautifulSoup
import requests as HTTP
def search_movie(id):
    search_url = f'https://myflixerz.to/movie/{id}'
    search = HTTP.get(search_url)
    search_data = search.text
    soup = BeautifulSoup(search_data, 'html.parser')

    image = soup.find('img', class_='film-poster-img')
    if image and image.has_attr('src'):
        src = image['src']
        img = src.split('"')[-1]
    else:
        'No image found!'
    description = soup.find('div', class_='description')
    desc = description.text.strip() if description else "No description avilable!"
    elements = soup.find_all('div', class_='elements')
    movie_details = []

    for el in elements:
        links = el.find('div', class_='row')
        det = links.find_all('div', class_='row-line')
        for d in det:
            details = ' '.join(d.text.split())
            movie_details.append(details)

    Released_date = movie_details[0] if len(movie_details) > 0 else "N/A"
    Genre = movie_details[1] if len(movie_details) > 1 else "N/A"
    cast = movie_details[2] if len(movie_details) > 2 else "N/A"
    duration = movie_details[3] if len(movie_details) > 3 else "N/A"
    country = movie_details[4] if len(movie_details) > 4 else "N/A"
    return Released_date, Genre, cast, duration, country, desc,img