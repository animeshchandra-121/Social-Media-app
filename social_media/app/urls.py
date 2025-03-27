from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('signup/', views.register, name= 'Register'),
    path('login/', views.login_page, name= 'login'),
    path('logout/', views.logout_page,name='logout'),
    path('social/', include('social.urls', namespace='social'))
]