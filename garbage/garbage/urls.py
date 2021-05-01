'''
Author: Gtylcara.
Date: 2021-04-26 14:10:32
LastEditors: Gtylcara.
LastEditTime: 2021-04-26 23:23:11
'''
"""garbage URL Configuration

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
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', views.login),
    path('api/register', views.register),
    path('api/register/checkSMS', views.checkSMS),
    path('api/register/checkphone', views.getSMS),
    path('api/userInfo', views.login),
    path('api/thirdparty', views.thirdParty),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
