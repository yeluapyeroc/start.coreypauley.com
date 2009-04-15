from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
####### Static Media Serving #######
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/yeluapyeroc/programming/web/start.coreypauley.com/httpdocs/media'}),

####### AJAX Requests #######
	(r'^basiccommands/$', 'start.Page.views.json_get_basic_commands'),
    (r'^advancedcommands/$', 'start.Page.views.json_get_advanced_commands'),
    (r'^bookmarks/$', 'start.Page.views.json_get_bookmarks'),

####### Advanced Commands #######
    (r'^advanced/ab/$', 'start.Command.views.add_bookmark'),

####### Site Urls #######
    (r'^$', 'start.Page.views.start'),

####### Admin #######
    (r'^admin/(.*)', admin.site.root),
)
