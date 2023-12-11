from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

URL ="https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

combined_cases = []

def fetch():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    row = soup.find('table')
    row = row.find('tbody')
    row = row.find_all('tr')[:-1] #skip the last one
    country_names = []
    total_cases = []
    total_deaths = []
    tmp = []
    for i in range(1,100):
        th = row[i].find('th')
        country_names.append(th.text.strip())
        tds = row[i].find_all('td')[1:] #skip the first one
        total_cases.append(tds[0].text.strip())
        total_deaths.append(tds[1].text.strip())

    for i in range(1,99):
        tmp.append(country_names[i]) #India
        tmp.append(total_cases[i]) #100
        tmp.append(total_deaths[i]) #1
        combined_cases.append(tmp) #[India,100,1]
        tmp = []

fetch() #call
print(combined_cases)

def index(req):
    return render(req, 'myapp/index.html', {
        'combined_cases' : combined_cases
    })
    
