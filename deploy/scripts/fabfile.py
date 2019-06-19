#-*-coding:utf-8-*-
#__autor__ = 'bruse zhou'
from fabric.api import *
from datetime import datetime
time=datetime.now().strftime('%Y-%m-%d_%H%M%S')
env.hosts = ['192.168.182.140']            # 指定 hosts 远程主机
# env.key_filename = '/c/Users/Administrator/.ssh/id_rsa'     # 指定你的私钥文件
# env.user = 'root'                    # 指定用户名
env.user = 'root'
env.password = '123456'
def tarfile():                         # 随便创建一个任务，用来测试
    run('tar zcvf /tmp/www.txt /tmp/www.txt_%s'%time)
