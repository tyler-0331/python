from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"
data = req.urlopen(url)

soup = BeautifulSoup(data,'lxml')

st1 = soup.select("#tabCont01 > ul > li > a > dl > dt")
st2 = soup.select("#tabCont01 > ul > li> a > p.money > strong")

name = list()
price = list()
for s in st1:
    if s.string:
        name.append(s.string)
for p in st2:
    if p.string:
        tmp = p.text.strip()
        tmp = tmp.replace(',','')
        price.append(int(tmp))
# print(name)
# print(price)

df = pd.DataFrame({'상품명': name, '가격': price})
print(df.head(2))
print(df['가격'].mean())
print(df['가격'].std())


# from bs4 import BeautifulSoup
# import urllib.request
# import pandas as pd
# url = "http://www.kyochon.com/menu/chicken.asp"
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page.read(), "html.parser")
# ss1 = soup.select("#tabCont01 > ul > li > a > dl > dt")
# ss2 = soup.select("#tabCont01 > ul > li> a > p.money > strong")
# cn = list()
# price = list()
# for s in ss1:
#     if s.string:
#         cn.append(s.string)
# for p in ss2:
#     if p.string:
#         tmp = p.text.strip()
#         tmp = tmp.replace(',','')
#         price.append(int(tmp))
#
# print(cn)
# print(price)
#
# df = pd.DataFrame({'상품명': cn, '가격': price})
# print(df)
# print(df['가격'].mean())
# print(df['가격'].std())


# import MySQLdb
# import pickle
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# try:
#     with open('mydb.dat', mode = 'rb') as obj:
#         config = pickle.load(obj)
# except Exception as e:
#     print('연결오류:',e)
#
# try:
#     conn = MySQLdb.connect(**config)
#     cursor = conn.cursor()
#     sql = """
#     select buser_name, jikwon_gen, jikwon_pay
#     from jikwon inner join buser on buser_no=buser_num
#     """
#     cursor.execute(sql)
#
#     df1 = pd.DataFrame(cursor.fetchall(), columns=['부서명','성별','연봉'])
#     print(df1.head(2))
#
#     jik_ypay = df1.groupby(['성별'])['연봉'].mean()
#     print(jik_ypay)
#
#     plt.rcParams['axes.unicode_minus'] = False
#     plt.bar(range(len(jik_ypay)), jik_ypay)
#     plt.xlabel('연봉')
#     plt.xticks([0,1], labels=['Male', 'Female'])
#     plt.ylabel('부서별')
#     plt.title('gender')
#     plt.show()
#
# except Exception as e:
#     print('처리오류:',e)
# finally:
#     cursor.close()
#     conn.close()