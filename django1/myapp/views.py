from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(requst):
    # return HttpResponse('요청 처리 결과')
    
    msg = '장고 만세?!'
    ss = "<html><body>장고 프러젝트 구현 %s</body></html>"%msg
    return HttpResponse(ss)

def showFunc(request):
    msg = '파이썬 쒯쒯!'
    
    return render(request,'show.html' ,{'mymsg':msg})  # forward 방식




