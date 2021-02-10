import requests
from bs4 import BeautifulSoup


def fetch_data() -> dict:
    """
    This function receives data from the site and fills the dictionary with it.
    :return: A dictionary containing the names of the authors as a key and an array of their books as a value .
    """
    data = {}
    headers = {'User-Agent': 'Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'
                             ' Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4'}

    try:
        response = requests.get('http://lit-classic.ru/', headers=headers)
    except requests.RequestException as e:
        print(e)
        return data

    html_handler = BeautifulSoup(response.text, 'html.parser')
    html_authors_section = html_handler.findAll('li')
    books_count = 0

    for i in html_authors_section:
        # Only direct children (recursive=False)
        html_author_element = i.findChildren("a", recursive=False)

        response = requests.get(html_author_element[0]['href'], headers=headers)
        html_handler = BeautifulSoup(response.text, 'html.parser')
        html_books_section = html_handler.findAll("div", {"class": "txt"})
        books_array = []

        for j in html_books_section:
            html_book_element = j.findChildren("a", recursive=False)
            books_array.append(html_book_element[0].contents[0])

        data[html_author_element[0].contents[0]] = books_array
        books_count += len(books_array)

    print('Fetched', len(data.keys()), 'authors with', books_count, 'books')
    return data
