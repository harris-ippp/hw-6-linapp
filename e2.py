#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

url_va = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req_va = requests.get(url_va)
html_va = req_va.content #getting the contents of the website
soup = BeautifulSoup(html_va,'html.parser') #turning it into a soup object so you can manipulate in python
tags = soup.find_all('tr','election_item')

ELECTION_ID=[]
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    i=[year,year_id]
    ELECTION_ID.append(i)
    #print(year, year_id)
Year = [item[0] for item in ELECTION_ID]
ID = [item[1] for item in ELECTION_ID]
k = dict(zip(ID, Year))
k

for t in ID:
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    replace_url = base.format(t)
    response = requests.get(replace_url).text
    Year_data = "president_general_"+ k[t] +".csv"
    with open(Year_data, 'w') as output:
        output.write(response)
