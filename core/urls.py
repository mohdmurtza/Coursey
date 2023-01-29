from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('getstarted/',views.getstarted,name='getstarted'),
    path('courses/',views.courses,name='courses'),
    path('teachers/',views.teachers,name='teachers'),
    
]
