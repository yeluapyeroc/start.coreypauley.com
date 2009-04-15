from django.http import HttpResponse
from django.utils import simplejson
from start.Bookmark.models import Bookmark
from start.Command.models import Advanced
import re

def add_bookmark(request):
    if request.method == 'GET':
        key = request.GET['key']
        url = request.GET['url']
        ### Validate Url ###
        if not re.match(r'^(?#Protocol)(?:(?:ht|f)tp(?:s?)\:\/\/)(?#Username:Password)(?:\w+:\w+@)?(?#Subdomains)((?:(?:[-\w]+\.)+(?#TopLevel Domains)(?:com|org|net|gov|mil|biz|info|mobi|name|aero|jobs|museum|travel|[a-z]{2}))|(?#IP Address)(?:\d{1,3}\.){3}\d{1,3})(?#Port)(?::[\d]{1,5})?(?#Directories)(?:(?:(?:/(?:[-\w~!$+|.,=]|%[a-f\d]{2})+)+|/)+|\?|#)?(?#Query)(?:(?:\?(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)(?:&(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)*)*(?#Anchor)(?:#(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)?$', url):
            return HttpResponse(simplejson.dumps({'success': False, 'message': 'Not a valid url'}), mimetype='application/json')

        new_bookmark, created = Bookmark.objects.get_or_create(user=request.user, command=key)
        if created:
            new_bookmark.url = url
            new_bookmark.save()
            return HttpResponse(simplejson.dumps({'success': True, 'message': 'Bookmark added successfully'}), mimetype='application/json')
        else:
            return HttpResponse(simplejson.dumps({'success': False, 'message': 'Bookmark with that key already exists'}), mimetype='application/json')
