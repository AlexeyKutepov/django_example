from django.conf.urls import patterns, include, url
from async.views import request_handler
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    #Наша страница
    url(r'^$', request_handler),
)
