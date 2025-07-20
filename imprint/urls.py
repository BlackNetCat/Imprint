from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('tools/', views.tools, name='tools'),
    path('about/', views.about, name='about')
]