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

#loop through thead, put all the headers into list as strings
header_row = []
for header in thead.findAll('th'):
    strheader = str(header)
    cleanHeader = re.sub('<\w+>|</\w+>','',strheader)
    header_row.append(cleanHeader)

#declare variables used for tbody looping
numLists = len(tbody.findAll('tr'))
depth = [[]]*numLists
counter = 0

#loop through tbody, find all th and td. convert to strings, remove html tags, dynamically create lists depending on how many tr's
for i in tbody.findAll('tr'):
    info = tbody.findAll(['th','td'])
    for data in info:
        strdata = str(data)
        noTag = re.sub('<\w+>|</\w+>','',strdata)
        depth[counter].append(noTag)

    counter+= 1

#zip header_row and spec_row into a dict to match each key with its corresponding value 
# loop through tbody entries, for each one, zip to the headers list, output that to external file     
for x in range(len(depth)):
    final = dict(zip(header_row,depth[x]))
    with open('/Users/willwhite/Documents/dataTests/test.json','w') as json_file:
        json.dump(final,json_file)
