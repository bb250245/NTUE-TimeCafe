"""bakeproj URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url


from myapp.views import home, menu, aboutUs
from product import views as pviews
from CookieSessionApp import views as csviews
from cart import views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('menu/',menu),
    path('aboutUs/',aboutUs),
    path('order/',pviews.product),
    path('order/<slug:slug>/', pviews.detail, name='detail'),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),

    # cookies
    path('set_cookie/<str:key>/<str:value>/', csviews.set_cookie),
    path('set_cookie2/<str:key>/<str:value>/', csviews.set_cookie2),
    path('get_cookie/<str:key>/', csviews.get_cookie),
    path('get_allcookies/', csviews.get_allcookies),
    path('delete_cookie/<str:key>/', csviews.delete_cookie),
    path('pagecount/', csviews.pagecount),
    # sessions
    path('set_session/<str:key>/<str:value>/', csviews.set_session),
    path('get_session/<str:key>/', csviews.get_session),
    path('get_allsessions/', csviews.get_allsessions),
    # vote
    path('vote/', csviews.vote),    
    path('set_session2/<str:key>/<str:value>/', csviews.set_session2),
    path('delete_session/<str:key>/', csviews.delete_session),
    # login
    path('login/', csviews.login),  
    path('logout/', csviews.logout),

    path('mypage/', csviews.mypage),
    path('adduser/', csviews.adduser),
    path('register/', csviews.register),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
