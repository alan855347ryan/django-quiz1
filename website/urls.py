
from django.urls import path
from . import views

urlpatterns = [
		path('',views.home,name="home"),
		path('generalknowledge.html',views.generalknowledge,name="generalknowledge"),
    	path('history.html',views.history,name="history"),
    	path('about.html',views.about,name="about"),
    	path('results.html',views.results,name="results"),
    	path('results2.html',views.results2,name="results2"),
   
]
