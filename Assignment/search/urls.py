from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name= 'search')
]