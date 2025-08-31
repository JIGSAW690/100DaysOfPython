import bs4
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = bs4.BeautifulSoup(yc_web_page, 'html.parser')
#print(soup.prettify())

article_tags = soup.find_all(name='span', class_='titleline')
for i in range(len(article_tags)):
    article_text = article_tags[i].getText()
    print(article_text)
article_link = soup.select(selector='span a')
for i in range(9, len(article_link)):
    print(article_link[i].get('href'))
article_upvote = soup.find_all(name='span', class_='score')
for i in range(len(article_upvote)):
    print(article_upvote[i].getText())
