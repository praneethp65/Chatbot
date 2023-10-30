import requests
import random
from bs4 import BeautifulSoup
def check(s, l):
    if s in l:
        rc = random.choice(show).get_text().strip()
        return(check(rc, l))
    else:
        return s
recs = input('Do you want General recommendation or by Streaming service? ').upper()
if recs == 'GENERAL' or recs == 'GENERAL RECOMMENDATION':
    x = random.randint(1, 25)
    page = requests.get('https://www.tvguide.com/streaming/all/documentary/show/1/?sort=highestRated&genre=documentary&type=show&releaseYearMin=2000&releaseYearMax=2021&page={0}'.format(x))
    soup = BeautifulSoup(page.content, 'html.parser')
    show = list(soup.select('h3 a'))
    l = []
    for i in range(0, 10):
        c = random.choice(show).get_text().strip()
        c = check(c, l)
        l.append(c)
    for i in l:
        print(i)
elif recs == 'STREAMING SERVICE' or recs == 'STREAMING':
    ott = input('Do you want shows from Netflix, Prime or Hbo? ').title()
    if ott == 'Netflix':
        y = random.randint(1, 10)
        page = requests.get('https://www.tvguide.com/streaming/netflix/documentary/show/1/?sort=highestRated&network=netflix&genre=documentary&type=show&releaseYearMin=2000&releaseYearMax=2021&page={0}'.format(y))
        soup = BeautifulSoup(page.content, 'html.parser')
        show = list(soup.select('h3 a'))
        l = []
        for i in range(0, 10):
            c = random.choice(show).get_text().strip()
            c = check(c, l)
            l.append(c)
        for i in l:
            print(i)
    elif ott == 'Prime':
        z = random.randint(1, 4)
        page = requests.get('https://www.tvguide.com/streaming/amazon-prime/documentary/show/1/?sort=highestRated&network=amazon-prime&genre=documentary&type=show&releaseYearMin=2000&releaseYearMax=2021&page={0}'.format(z))
        soup = BeautifulSoup(page.content, 'html.parser')
        show = list(soup.select('h3 a'))
        l = []
        for i in range(0, 10):
            c = random.choice(show).get_text().strip()
            c = check(c, l)
            l.append(c)
        for i in l:
            print(i)
    elif ott == 'Hbo':
        b = random.randint(1, 4)
        page = requests.get('https://www.tvguide.com/streaming/hbo-max/documentary/show/1/?sort=highestRated&network=hbo-max&genre=documentary&type=show&releaseYearMin=2000&releaseYearMax=2021&page={0}'.format(b))
        soup = BeautifulSoup(page.content, 'html.parser')
        show = list(soup.select('h3 a'))
        l = []
        for i in range(0, 10):
            c = random.choice(show).get_text().strip()
            c = check(c, l)
            l.append(c)
        for i in l:
            print(i)
    else:
        print("Sorry, we don't recognize that streaming service")
else:
    print("Sorry, we don't understand")
