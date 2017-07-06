from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from underten import views
from underten.views import hello
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^article/', include('article.urls', namespace="article")),
    url(r'^product/', include('product.urls', namespace="product")),

    url(r'^$', include('article.urls', namespace="root")),
    url(r'^hello/$', hello),

    url(r'^accounts/', include('account.urls', namespace="account")),

    url(r'^summernote/', include('django_summernote.urls')),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()