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
    page = requests.get('https://www.tvguide.com/streaming/all/drama/show/1/?sort=highestRated&genre=drama&type=show&releaseYearMin=2000&releaseYearMax=2022&page={0}'.format(x))
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
        y = random.randint(1, 15)
        page = requests.get('https://www.tvguide.com/streaming/netflix/drama/show/1/?sort=highestRated&network=netflix&genre=drama&type=show&releaseYearMin=1999&releaseYearMax=2021&page={0}'.format(y))
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
        z = random.randint(1, 8)
        page = requests.get('https://www.tvguide.com/streaming/amazon-prime/drama/show/1/?sort=highestRated&network=amazon-prime&genre=drama&type=show&releaseYearMin=1999&releaseYearMax=2021&page={0}'.format(z))
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
        b = random.randint(1, 5)
        page = requests.get('https://www.tvguide.com/streaming/hbo-max/drama/show/1/?sort=highestRated&network=hbo-max&genre=drama&type=show&releaseYearMin=1999&releaseYearMax=2021&page={0}'.format(b))
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
