"""treasure_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('clue1/',views.clue1Page,name='clue1'),
    path('index/',views.indexPage,name='index'),
    path('clue2/',views.clue2Page,name='clue2'),
    path('clue3/',views.clue3Page,name='clue3'),
    path('clue4/',views.clue4Page,name='clue4'),
    path('clue6/',views.clue6Page,name='clue6'),
    path('clue7/',views.clue7Page,name='clue7'),
    path('clue8/',views.clue8Page,name='clue8'),
    path('clue9/',views.clue9Page,name='clue9'),
    path('clue5/',views.clue5Page,name='clue5'),
    path('adm/',views.admPage,name='adm'),
    path('winner/',views.winnerPage,name='winner'),
    path('oops/',views.oopsPage,name='oops'),
]
