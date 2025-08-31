from bs4 import BeautifulSoup
import lxml

with open('website.html', 'r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tags in all_anchor_tags:
    print(tags.getText())
    print(tags.get('href'))

head = soup.find(name='h1', id='name')
print(head)

section_head = soup.find(name='h3', class_='heading')
print(section_head)

company = soup.select_one(selector='p a')
print(company)

other_anchor = soup.select(selector='.heading')
print(other_anchor)