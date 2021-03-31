from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('newnote', views.newnote, name="newnote"),
    path('delnote/<int:nid>', views.delnote, name="delnote"),
    path('editnote/<int:nid>', views.editnote, name="editnote")

    
]
