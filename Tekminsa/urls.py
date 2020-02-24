"""Tekminsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Pages import views as pv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pv.homepage, name='homepage'),
    path('about/', pv.about, name='about'),
    path('user_agreement/', pv.user_agreement, name='accounts agreement'),
    path('contact_us/', pv.contact_us, name='contact us'),
    path('cookie_policy/', pv.cookie_policy, name='cookie policy'),
    path('privacy_policy/', pv.privacy_policy, name='privacy policy'),
    path('community_guidelines/', pv.community_guidelines, name='community guidelines'),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
   ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
