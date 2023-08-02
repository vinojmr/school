from . import views
from django.urls import path


urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('new/', views.new, name='new_page'),
    path('form/', views.form, name='form'),
    path('success/', views.success_page, name='success_page'),
    path('engineer/', views.engineer, name='engineer'),
    path('medical/', views.medical, name='medical'),
    path('law/', views.law, name='law'),
    path('commerce/', views.commerce, name='commerce'),
    path('hospitality/', views.hospitality, name='hospitality'),
]