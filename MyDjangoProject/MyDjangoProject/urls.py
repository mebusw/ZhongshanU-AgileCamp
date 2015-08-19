from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'OnlineExchange.views.begin', name='begin'),
    url(r'^dashboard', 'OnlineExchange.views.dash', name='dashboard'),
    url(r'^login', 'OnlineExchange.views.login', name='login'),
    url(r'^category', 'OnlineExchange.views.getCategory', name='category'),
    url(r'^register', 'OnlineExchange.views.register', name='register'),
    url(r'^myproduct', 'OnlineExchange.views.getMyProduct', name='myproduct'),
    url(r'^logout', 'OnlineExchange.views.logout', name='logout'),
)
