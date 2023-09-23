from django.urls import path
from . import views
urlpatterns=[

    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('chatbot',views.chatbot,name='chatbot'),
    path('add',views.add,name='add'),
    path('login',views.logi,name='login'),
    path('logout',views.log,name='logout')
]