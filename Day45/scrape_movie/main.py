import requests, os
from bs4 import BeautifulSoup

MOVIES_ENDPOINT = os.environ.get('MOVIES_ENDPOINT')

response = requests.get(MOVIES_ENDPOINT)
best_movies_webpage = response.text
movie_list = []

soup = BeautifulSoup(best_movies_webpage, 'html.parser')

movie_tags = soup.select(selector='h2 strong')
for i in range(len(movie_tags)):
    movie_name = movie_tags[i].getText()
    #print(movie_name)
    movie_list.append(movie_name)

with open('movies.txt', 'w') as file:
    file.write('\n'.join(movie_list[::-1]))



