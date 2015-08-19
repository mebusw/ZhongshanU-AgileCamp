# urls.py
from django.conf.urls import include , url , patterns

urlpatterns = patterns ('sina.views',
    url(r'^$', 'index' ),
)