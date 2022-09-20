from django.urls import path
from . import views

urlpatterns = [
    path('',views.loadfirst, name='loadfirst'),
    path('equal',views.equal,name='equal'),
]
