import requests
from bs4 import BeautifulSoup
from lxml import html

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
    head = x.text.strip()
    url = base_url+x['href']
    info = {'title':head, 'url':url}
    python.append(info)

with open("scrape.txt", "w") as file:
    for x in python:
        file.write(str(x))
