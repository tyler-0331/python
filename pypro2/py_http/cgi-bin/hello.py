# 웹용 파이썬 모듈
a = 10
b = 20
c = a + b
mbc = '파이썬 만세?!'

print('Content-Type: text/html;charset=utf-8\n')
print('<html><body>')
print('<b>안녕하세요</b> 파이썬 모듈로 작성한 문서입니다.<br> ') # 여러칸 띄고 싶을떄 &nbsp
print('<hr>')
print('합은 %d'%(c,))
print('<br>메세지는 %s'%mbc)
print('<p>작성자: 홍길동')
print('</body></html>')








