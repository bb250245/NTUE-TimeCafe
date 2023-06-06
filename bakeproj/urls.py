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


from myapp.views import home, menu, aboutUs, Login
from product import views as pviews
#from cart import views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('menu/',menu),
    path('aboutUs/',aboutUs),
    path('Order/',pviews.product),
    path('Order/<slug:slug>/', pviews.detail, name='detail'),
    path('Login/',Login),
    #path('cart/', include(('cart.urls','cart'), namespace='cart')),
    #path('addcart/<int:product_id>/', cviews.AddCartView.as_view(), name='add_cart'),
    #path('deletecart/<int:product_id>/', cviews.DeleteCartView.as_view(), name='delete_cart'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
