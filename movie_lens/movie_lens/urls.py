"""movie_lens URL Configuration

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
from movieratings.views import index_view, top_movies_view, movie_view, rater_view, movie_detail, rater_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r'^top_movies/$', top_movies_view),
    url(r'^movies/$', movie_view),
    url(r'^raters/$', rater_view),
    url(r'^rater_detail/(?P<rater_id>\d+)/$', rater_detail),
    url(r'^movie_detail/(?P<movie_id>\d+)/$', movie_detail),
]
