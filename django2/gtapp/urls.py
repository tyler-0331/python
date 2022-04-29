# main urls.py로 부터 위임받은 urls
from django.urls import path
from gtapp import views  # 자기 영역에 있어도 꼭 import 하기!!!

urlpatterns = [
    path('insert', views.insertFunc), 
    # path('insertok', views.insertokFunc), 
    
]


