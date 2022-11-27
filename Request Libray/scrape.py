import requests
from bs4 import BeautifulSoup
import json

def scrape(base_url):
    python = []

    for x in range(1, 10):
        try:
            response = requests.get(base_url+'?page='+str(x))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise e
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            link = soup.findAll('a', attrs={"class":"text-bold wb-break-word"}, href=True)
            for x in link:
                info= {}
                head = x.text.strip()
                url = base_url+x['href']
                info[head] = url
                python.append(info)

    with open('scrape.json', 'a') as file:
        json.dump(python, file, indent=2)

def check_url(base_url):
    try:
        response = requests.get(base_url)
    except requests.exceptions.RequestException as e:
        raise e
    else:
        scrape(base_url)
  

if __name__ == "__main__":
    check_url(base_url='https://github.com/topic/python')
