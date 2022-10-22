f = open('ip2.txt','a+')

for i in range(8801,8820):
    ip = '192.168.23.133:'+str(i)
    f.write(ip+'\n')
    print(ip)
