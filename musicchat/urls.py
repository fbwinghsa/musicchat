from django.conf.urls import patterns, include, url

from django.contrib import admin
import musicchat.view;
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musicchat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^service/$', musicchat.view.interface),

    #url(r'^admin/', include(admin.site.urls)),
)
