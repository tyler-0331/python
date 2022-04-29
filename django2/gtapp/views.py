from django.shortcuts import render
from django.views.generic.base import TemplateView   # Class-based views 쓸때 임포트!
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, "index.html") 

class CallView(TemplateView):     # Class-based views 쓸때는 TemplateView를 상속 받아서 .as_views를 사용!!
    template_name = "callget.html"

'''
def insertFunc(request):
    return render(request, 'insert.html')


def insertokFunc(request):
    #irum = request.GET.get('name') 1번
    irum = request.GET['name']    # 2번 
    print(irum)
    return render(request,'list.html',{'irum':irum})
'''
    # get 과 post를 구분해서 하나의 function으로 넣어두기! 
def insertFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request, 'insert.html')  # forwarding 방식
        
    elif request.method == 'POST':
        print('POST 요청 처리')
        irum = request.POST.get('name')
        return render(request,'list.html',{'irum':irum})
    else:
        print('요청 에러') 


