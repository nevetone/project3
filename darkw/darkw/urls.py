"""darkw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from main.views import index, status
from auth_user.views import logout_view, login_view, registration_view
from organization.views import organization, management
from profiles.views import profiles, tests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('status/', status, name="status"),
    path('logout/', logout_view, name="logout_view"),
    path('loggin/', login_view, name="login_view"),
    path('register/', registration_view, name="registration_view"),
    path('status/organization/', organization, name="organization"),
    path('status/organization/management/', management, name="management"),
    path('status/profiles/', profiles, name="profiles"),
    path('status/tests/', tests, name="tests"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)