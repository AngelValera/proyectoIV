from django.conf.urls import patterns, url
from merka import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^seccion/(?P<seccion_name_slug>[\w\-]+)/$', views.seccion, name='seccion'),

        )
