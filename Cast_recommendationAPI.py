import requests
import json
request = input("Enter the name: ").title()
if request == 'Michael' or request == 'Michael Scott' or request == 'Steve Carell' or request == 'Steve':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0136797")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Dwight' or request == 'Dwight Schrute' or request == 'Rainn Wilson' or request == 'Rainn':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0933988")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Pam' or request == 'Pam Beesly' or request == 'Jenna' or request == 'Jenna Fischer':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0278979")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Jim' or request == 'Jim Halpert' or request == 'John' or request == 'John Krasinski':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1024677")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Creed' or request == 'Creed Bratton':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0105588")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Stanley' or request == 'Stanley Hudson' or request == 'Leslie David Baker' or request == 'Leslie':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1534715")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Phyllis' or request == 'Phyllis Vance' or request == 'Phyllis Smith':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0809613")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Kevin' or request == 'Kevin Malone' or request == 'Brian' or request == 'Brian Baumgartner':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1580911")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Angela' or request == 'Angela Martin' or request == 'Angela Kinsey':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1526554")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Meredith' or request == 'Meredith Palmer' or request == 'Kate' or request == 'Kate Flannery':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0281212")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Oscar' or request == 'Oscar Martinez' or request == 'Oscar Nuñez':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1386645")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Kelly' or request == 'Kelly Kapoor' or request == 'Mindy' or request == 'Mindy Kaling':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1411676")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Ryan' or request == 'Ryan Howard' or request == 'Novak' or request == 'B.J.Novak':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1145983")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Andy' or request == 'Andy Bernard' or request == 'Andrew Bernard' or request == 'Ed' or request == 'Ed Helms':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm1159180")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Toby' or request == 'Toby Flenderson' or request == 'Paul' or request == 'Paul Lieberstein':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0509425")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Darryl' or request == 'Darryl Philbin' or request == 'Craig' or request == 'Craig Robinson':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0732497")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Ellie' or request == 'Ellie Kemper' or request == 'Erin' or request == 'Erin Hannon':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm2608689")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Jan' or request == 'Jan Levinson' or request == 'Melora' or request == 'Melora Hardin':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0002124")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'David' or request == 'David Wallace' or request == 'Andy Buckley' or request == 'Wallace':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm2952467")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Karen' or request == 'Karen Filippelli' or request == 'Rashida' or request == 'Rashida Jones':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0429069")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Roy' or request == 'Roy Anderson' or request == 'David Denman':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0219292")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
elif request == 'Holly' or request == 'Holly Flax' or request == 'Amy' or request == 'Amy Ryan':
    response = requests.get("https://imdb-api.com/API/Name/k_uesz1sa9/nm0752407")
    z = response.json()['knownFor']
    Recs = []
    for i in z:
        l = i['fullTitle']
        Recs.append(l)
    for s in Recs:
        print(s)
else:
    print("Sorry, we don't recognize that name")
