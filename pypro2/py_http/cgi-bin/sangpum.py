# DB 자료 출력
import MySQLdb
import pickle

with open('mydb.dat','rb') as obj:
    config = pickle.load(obj)
    
print('Content-Type: text/html;charset=utf-8\n')  
print('<head><body>')
print('<h2>상품 정보</h2>')
print('<table border ="1"><tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>')
try:
    conn = MySQLdb.connect(**config)    # dict type 이어서 packing 연산자에 **
    cursor = conn.cursor()
    
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    
    for code, sang, su, dan in datas:
        print('''
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        <tr>
        '''.format(code, sang, su, dan))
except Exception as e:
    print('처리오류: ', e)
finally:
    cursor.close()
    conn.close()
print('</table>')
print('<br>')
print("<a href='../main.html'>메인으로</a>")
print('</body></head>')













