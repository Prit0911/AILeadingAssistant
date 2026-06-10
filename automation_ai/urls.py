from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.base, name='base'),
    path('',views.index,name='index'),
    path('query/',views.query, name='query'),
    path('about/',views.about, name='about')
]