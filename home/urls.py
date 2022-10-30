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
    path('processors',views.pList, name="processors"),
    path('gpu',views.gList, name="gpu"),
    path('ram',views.rList, name="ram"),
    path('ssd',views.sList, name="ssd"),
    path('hdd',views.hList, name="hdd"),
    path('mobo',views.mList, name="mobo"),
    path('mkpc',views.makePC, name="makepc"),
]
# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)