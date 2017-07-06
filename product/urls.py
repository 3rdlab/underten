from django.conf.urls import patterns, url

from product import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^reviews/$', views.ReviewIndexView.as_view(), name='review_index'),
    url(r'^reviews/(?P<pk>\d+)/$', views.ReviewDetailView.as_view(), name='review_detail'),
	url(r'^reviews/add$', views.review_add, name='review_add'),

	url(r'^brand/(?P<brand>[a-zA-Z\d]+)/$', views.BrandIndexView.as_view(), name='brand_index'),
)