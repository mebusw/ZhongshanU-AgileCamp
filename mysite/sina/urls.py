from django.conf.urls import include, url,patterns

from sina import views

# urlpatterns = patterns('sina.views',
# 	url(r'^$', 'index'),
# 	url(r'^denglu$', 'denglu'),
# 	)

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^gonglv/$',views.gonglv,name = 'gonglv'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^findguider/$',views.findguider,name = 'findguider'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^doguider/$',views.doguider,name = 'doguider'),
	url(r'^question$', views.question, name = 'question'),
    url(r'^answer$', views.answer, name = 'answer'),
	url(r'^gonglvcontent$', views.gonglvcontent, name = 'gonglvcontent'),
	url(r'^liuyanban$', views.liuyanban, name = 'liuyanban'),
)