from django.conf.urls import url
from django.conf.urls import patterns, include
from . import views
from merka2.views import raiz, crear


urlpatterns = [
	url(r'^$', raiz),
	url(r'^crear/', 'merka2.views.crear', name='crear'),
]
#url(r'^$', views.IndexView.as_view(), name='index'),
