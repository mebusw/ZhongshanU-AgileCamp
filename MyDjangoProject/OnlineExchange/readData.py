__author__ = 'lixin77'
# -*-coding:utf-8-*-

from OnlineExchange.models import Product
from random import randint

fp = open('data.txt', 'r')
for line in fp:
    line = line.strip('\n')
    contents = line.split('\t')
    uname = contents[0]
    pname = contents[1]
    uid = randint(1, 10000000)
    pid = randint(1, 10000000)
    date = contents[2]
    status = int(contents[3])
    des = contents[4]
    url = contents[5]
    type = int(contents[6])
    p = Product(uid=uid, pid=pid, pname=pname, uname=uname, date=date, status=status, description=des, type=type, url=url)
    p.save()


