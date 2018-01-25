
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('home.urls')),
    url(r'^course/',include('course.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^alumini/',include('alumini.urls')),
    url(r'^current/',include('current.urls')),
]
