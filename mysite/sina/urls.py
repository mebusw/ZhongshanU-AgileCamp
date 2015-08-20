from django.conf.urls import include, url,patterns

from sina import views

# urlpatterns = patterns('sina.views',
# 	url(r'^$', 'index'),
# 	url(r'^denglu$', 'denglu'),
# 	)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^gonglv/$',views.gonglv,name = 'gonglv'),
    url(r'^findguider/$',views.findguider,name = 'findguider'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^doguider/$',views.doguider,name = 'doguider'),
	url(r'^question$', views.question, name = 'question'),
	url(r'^gonglvcontent$', views.gonglvcontent, name = 'gonglvcontent'),
        url(r'^answer$', views.answer, name = 'answer'),
)
