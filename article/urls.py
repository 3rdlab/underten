from django.conf.urls import patterns, url, include

from article import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add_new/$', views.add_new, name='add_new'),
	
	url(r'^category/(?P<category>[a-zA-Z\d]+)/$', views.CategoryIndexView.as_view(), name='category_index'),

)