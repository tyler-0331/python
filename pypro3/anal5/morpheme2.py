# 위키백과 사이트에서 검색단어 관련 글 스크래핑 후 형태소 분석
import urllib
from bs4 import BeautifulSoup 
from konlpy.tag import Okt
from urllib import parse  #한글 인코딩요 모듈

okt = Okt()
para = parse.quote('이순신')    # 이순신을 디코딩해와서 읽은 글 대로 
print(para)
url = "https://ko.wikipedia.org/wiki/" + para
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(),'lxml')
# print(soup)

# 한글 형태소 분석으로 명사만 추출해 기억장소에 담기
wordlist = []
for item in soup.select("div#mw-content-text > div > p"):
    if item.string != None:
        # print(item.string)
        wordlist += okt.nouns(item.string)

print('wordlist 출력:',wordlist)   # 피클로 저장해 두면 쓰기 편하다
print('단어 수: ', len(wordlist))
print('중복 제거 후 단어 수: ', len(set(wordlist)))  # set 에 넣어서 중복된 단어 제외

print()
word_dict = {}  # {"이순신":5 ...
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1 

print('word_dict 출력:',word_dict)

import pandas as pd
print('DataFrame데 담기 ----------')
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head(3))
print()
df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
print(df2)
df2 = df2.T    # 행 열 바꾸기
df2.columns =['단어','빈도수']
print(df2.head(5))

print('------------------------------------')
# 파일로 저장
df2.to_csv('이순신.csv', sep=',', index=False)

df3= pd.read_csv('이순신.csv')
print(df3)













