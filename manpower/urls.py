"""manpower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from manpowermanage import registlogin
from django.urls import path, include
from manpowermanage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test/', registlogin.test),
    # path('test/', views.test),
    # path('test2/', views.test2),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('login/', views.login),
    path('corp_settings/', views.corp_settings),
    path('setting_corp/', views.setting_corp),
    path('flush/', views.flush, name='flush'),
    path('edit_project/', views.edit_project),  ###
    path('edit_pro/', views.edit_pro),
    path('home/', views.home, name='home'),
    path('personalTasks/', views.PTasks),
    path('projectlist/', views.projectlist),
    path('search/', views.search),
    path('register/', views.regist),
    path('user_settings/', views.user_settings),
    path('setting_user/', views.setting_user),
    path('see_corp/',views.see_corp),
    path('new_Comment/',views.new_Comment),
    path('projectData/', views.projectData),
]
