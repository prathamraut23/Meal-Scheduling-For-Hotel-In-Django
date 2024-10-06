from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
   path('mfront', views.mfront,name='mfront'),
   path('managerlogin', views.managerlogin,name='managerlogin'),
   path('login', views.handlelogin,name='handlelogin'),
   path('logout', views.handlelogout,name='handlelogout'),
   path('additems', views.additems,name='additems'),
   path('delitem',views.delitem,name='delitem'),
   path('add',views.add,name='add'),
   path('delete',views.delete,name='delete'),
   path('history',views.history,name='history'),
]