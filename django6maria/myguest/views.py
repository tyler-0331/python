from django.shortcuts import render, redirect
from myguest.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request,'main.html')     # forwarding : 서버에서 서버 파일 직접 호출

def ListFunc(request):
    print(Guest.objects.filter(title__contains = '반가워')) # where 절을 추가 했다고 생각하면 됨 
    print(Guest.objects.filter(id = 1))
    print(Guest.objects.filter(title = '문안인사'))
    print(Guest.objects.get(id = 1))  # 1개 짜리를 읽을때 get사용
        
    gdatas = Guest.objects.all()
    # gdatas = Guest.objects.all().order_by('title') # ascending sort
    # gdatas = Guest.objects.all().order_by('-title') # descending sort
    # gdatas = Guest.objects.all().order_by('-id', 'title')[0:2] # id:descending  title: ascending
    
    return render(request,'list.html', {'gdatas':gdatas})

def InsertFunc(request):
    return render(request,'insert.html')



def InsertOkFunc(request):
    if request.method == "POST":
        # print(request.POST.get("title"))
        # print(request.POST["content"])
        Guest(
            title = request.POST.get("title"),
            content = request.POST.get("content"),
            regdate = datetime.now()  # timezone.now()
        ).save()    # insert into  ...
        
    # return HttpResponseRedirect('/guest')  # 추가 후 목록 보기    redirect 방식: 클라이언트를 통해 자료 요청 
    return redirect('/guest')  
        
"""  수정 
gtab= Guest.objects.get(id=해당아이디)
gtab.title = '수정제목'
gtab.content = '수정내용'
gtab.save()    "update 테이블명 set ...
"""
""" 삭제
gtab= Guest.objects.get(id=해당아이디)
gtab.delete()   " delete from 테이블명 ...
"""
        
        
        