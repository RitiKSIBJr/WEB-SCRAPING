import requests
from bs4 import BeautifulSoup
# from lxml import html
import os
import json
from collections import defaultdict

#request
base_url = "https://github.com/topics/python"


response = requests.get(base_url)

# Beautifulsoup4
soup = BeautifulSoup(response.text, 'html.parser')

#without css selectors
repo = soup.findAll("h3", attrs={"class":"f3 color-fg-muted text-normal lh-condensed"})

# with css selectors
# repos = soup.select("h3.f3 color-fg-muted text-normal lh-condensed")

# lxml
# tree = html.fromstring(response.text)
# title = tree.xpath('//h2[@class="blog-card__content-title"]/text()')
python = []


link = soup.findAll('a', attrs={"class":"text-bold wb-break-word"}, href=True)
for x in link:
    info = defaultdict()
    head = x.text.strip()
    url = base_url+x['href']
    info[head] = url
    python.append(dict(info))

with open('scrape.json', 'w') as file:
    json.dump(python, file, indent=2)

with open('scrape.json','r') as f:
    data = json.load(f)
