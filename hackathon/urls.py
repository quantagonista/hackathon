"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.views import login

from django.views import csrf



from hackathon import settings
from system.views import HomeView, logout_view, RegisterView, ProfilePage

urlpatterns = [

    url(r'^$', HomeView.as_view()),
    url(r'^accounts/logout/$', logout_view, name="logout"),
    url(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/profile/$', ProfilePage.as_view(), name="profile"),
    url(r'^admin/', admin.site.urls),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
            + static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)