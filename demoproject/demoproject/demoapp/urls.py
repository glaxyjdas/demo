from django.urls import path

from demoapp import views

urlpatterns = [

    path('', views.home, name='home'),
    path('add/',views.addition,name='addition'),
   # path('',views.contact,name='contact'),
   # path('detail/',views.detail,name='detail'),
   # path('',views.thanks,name='thanks')

]
