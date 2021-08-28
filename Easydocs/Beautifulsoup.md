# Beautiful docs

>A Python web scraping library

## Installation

>pip3 install bs4 

<br>

```
from bs4 import BeautifulSoup
import requests

content = requests.get("https://www.google.com").text

soup = BeautifulSoup(content, 'lxml')

soup.find('div', class_ = 'class_name')
```
