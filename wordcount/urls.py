#determines where the user request goes next 
#which html user get access to 
from django.urls import path
from . import views
urlpatterns = [
    #verb with location
    path('', views.homepage, name = 'home'),
    path('count/', views.count, name = 'count'),
    path('about/', views.about, name = 'about'),

]
