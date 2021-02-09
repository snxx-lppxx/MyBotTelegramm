import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4'}

response = requests.get('http://lit-classic.ru/', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.findAll('li')

for x in range(len(table)):
    children = table[x].findChildren("a", recursive=False)
    html_content = str(children[0])
    author_name = BeautifulSoup(html_content, 'html.parser')
    print(author_name.text)
