from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import index
from .views import signup
urlpatterns = patterns('sina.views',
#    url(r'^sina/', include('sina.urls')),		
#    url(r'^admin/', include(admin.site.urls)),
     url(r'^$','index'),
     url(r'^signup$','signup'),
)
