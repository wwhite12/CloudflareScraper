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
counter = 0
myDict = {}
for num in range(len(tbody.findAll('tr'))):
    myDict[num] = []
allTbody = tbody.findAll('tr')
#loop through tbody, find all th and td. convert to strings, remove html tags, dynamically create lists depending on how many tr's
for i in tbody.findAll('tr'):
    myList = []
    test = str(i)
    test.split("</tr>")
    info = allTbody[counter]
    for data in info:
        strdata = str(data)
        noTag = re.sub('<\w+>|</\w+>','',strdata)
        if noTag == '\n':
            continue
        myDict[counter].append(noTag)
          
    counter+= 1

#zip header_row and spec_row into a dict to match each key with its corresponding value 
# loop through tbody entries, for each one, zip to the headers list, output that to external file     
for set in range(len(myDict)):
    final = dict(zip(header_row,myDict[set]))
    with open('/insert/path/to/output/file','a+') as json_file:
       json.dump(final,json_file)
