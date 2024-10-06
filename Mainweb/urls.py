from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.frontpage,name='frontpage'),
    # path('manager', views.manager,name='manager'), 
    path('booking', views.booking,name='booking'),
    path('meal',views.meal,name='meal'),
    path('order',views.order,name='order'),

]