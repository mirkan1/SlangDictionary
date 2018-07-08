from django.conf.urls import url
from . import views

app_name = 'dictionary'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^explain/', views.explain, name='explain'),
	url(r'^other/', views.other, name='other'),
	url(r'^word/(?P<pk>\d+)/$', views.word_detail, name='word_detail'),
	#url(r'^explain/$', views.explain, name='explain'),
]