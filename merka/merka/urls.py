
from django.conf.urls import url
from django.conf.urls import patterns, include
from merka2.views import raiz, crear

urlpatterns = [
    # Examples:
    # url(r'^$', 'merka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', raiz),
    url(r'^crear/', 'merka2.views.crear', name='crear'),
    #url(r'^$', 'merka2.views.home', name='home')
]
