"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin

# You can either match a full URL (using ^ and $ in your regex), or part.
# This instruction makes the code go away and look at the urls.py file in the
# corresponding app.
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^', include('personal.urls'))
]

# Note: we make 'personal' the crux/homepage of our site, so rather than
# making the url regex r'^personal/', we make it r'^' (i.e. the website root).
# This MUST go at the end of the urlpatterns list, otherwise it will take precedence
# over more specific URLs.
