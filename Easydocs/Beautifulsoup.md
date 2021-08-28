# Beautiful docs

>A web scraping library

``
from bs4 import BeautifulSoup
import requests

content = requests.get("https://www.google.com").text

soup = BeautifulSoup(content, 'lxml')

soup.find('div', class_ = 'class_name')
```
