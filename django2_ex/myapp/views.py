from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")

def show(request):
    sex = request.GET['gen']
    return render(request,'show.html',{'sex':sex})
