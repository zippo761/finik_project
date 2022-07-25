import requests
from bs4 import BeautifulSoup

agent = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

query = 'Жалюзи-ролетта'

block_list = query.split()

url_query = '%20'.join(block_list)

url = 'https://www.google.ru/search?q=' + url_query + '&lr=213'

#print(url)

response = requests.get(url, headers=agent)

soup = BeautifulSoup(response.text, 'lxml')

for link in soup.findAll('a'):
    if 'market.yandex' in str(link.get('href')):
        print(link.get('href'))
        r = requests.get(link.get('href'), headers=agent)
        soup_inside = BeautifulSoup(r.text, 'lxml')
        print(soup_inside.prettify())
        break


