import urllib3
import json
from bs4 import BeautifulSoup
import re

https = urllib3.PoolManager()
#GET request to url, BeautifulSoup to return html table
cf_page = https.request('GET','https://developers.cloudflare.com/waf/change-log/scheduled-changes/')
cf_resp = cf_page.data.decode('utf-8')
soup = BeautifulSoup(cf_resp,'html.parser')
table = soup.find('table')
thead = table.find('thead')
tbody = table.find('tbody')

#loop through thead, put all the headers into an array as strings
header_row = []
for header in thead.findAll('th'):
    strheader = str(header)
    cleanHeader = re.sub('<\w+>|</\w+>','',strheader)
    header_row.append(cleanHeader)

spec_row = []
#print(tbody.findAll('tr'))
for i in tbody.findAll('tr'):
    info = tbody.findAll(['th','td'])
    for data in info:
        strdata = str(data)
        noTag = re.sub('<\w+>|</\w+>','',strdata)
        spec_row.append(noTag)

#zip header_row and spec_row into a dict to match each key with its corresponding value      
final = dict(zip(header_row,spec_row))
print(final)