

#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

from selenium import webdriver
# from alllists import alllist

driver = webdriver.Chrome()

def get_one_page(url):

    driver.get(url)
    html = driver.page_source
    return html


def next_page():
    for i in range(1,1666):  # 有一个翻页小技巧
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/ul/li[last()-1]/a').click()
        html = driver.page_source
        return html

def parse_page(html):
    big_list = []

    selector = etree.HTML(html)
    title = selector.xpath('/html/body/div[2]/div[1]/div[2]/ul/li/a/text()')
    links = selector.xpath('/html/body/div[2]/div[1]/div[2]/ul/li/a/@href')
    f_list = list(set(links)) #剔除重复项
    type = selector.xpath('/html/body/div[2]/div[1]/div[1]/a[2]/text()')

    f_type = len(title) *type

    for i1,i2,i3 in zip(title,f_list,f_type):
        big_list.append((i1,i2,i3))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='YunWei_PL',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into HongLian_linux (title,links,type) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    # for url in alllist:
    url ='http://www.linuxdiyf.com/articlelist.php?id=7&page=1'

    html = get_one_page(url)
    content = parse_page(html)
    insertDB(content)
    while True:
        try:

            html = next_page()
            content = parse_page(html)
            insertDB(content)
            print(datetime.datetime.now())
        except:
            pass

#
# create table HongLian_linux(
# id int not null primary key auto_increment,
# title text,
# links text,
# type varchar(20)
# ) engine=InnoDB  charset=utf8;


# drop  table HongLian_linux;



