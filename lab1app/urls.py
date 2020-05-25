from django.urls import path
from lab1app.views import *


app_name = 'lab1app'
urlpatterns = [    
	path('', index, name='home'),    
	path('index', index, name='index'),
	path('index2', index2, name='index2'), 
	path('index3', index3, name='index3'), 
] 