from django.urls import path
from mysurvey import views

urlpatterns = [
    path('survey',views.surveyView),
    path('surveyprocess', views.surveryProcess),
    path('surveyshow',views.dataAnalysis),
 
]