from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import index,verify, signup, signin, more, ask, getinfo, profile
urlpatterns = patterns('sina.views',
#    url(r'^sina/', include('sina.urls')),		
#    url(r'^admin/', include(admin.site.urls)),
     url(r'^$','index'),
     url(r'^signup$','signup'),
     url(r'^verify$','verify'),
     url(r'^signin$','signin'),
     url(r'^more$','more'),
     url(r'^ask$','ask'),
     url(r'^getinfo$','getinfo'),
     url(r'^profile$','profile'),

)
