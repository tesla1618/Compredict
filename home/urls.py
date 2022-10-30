from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name ="home"),
    path('login', views.signin, name = "login"),
    path('reg',views.reg, name='reg'),
    path('signout', views.signout, name="signout"),
]
