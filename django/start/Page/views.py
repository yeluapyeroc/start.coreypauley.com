from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers
from start.Command.models import Basic, Advanced
from start.Bookmark.models import Bookmark

def start(request):
    return render_to_response('start.html', {}, context_instance=RequestContext(request))

def json_get_basic_commands(request):
    data = serializers.serialize('json', Basic.objects.all())
    return HttpResponse(data, mimetype='application/json')

def json_get_advanced_commands(request):
    data = serializers.serialize('json', Advanced.objects.all())
    return HttpResponse(data, mimetype='application/json')

def json_get_bookmarks(request):
    data = serializers.serialize('json', Bookmark.objects.filter(user__username=request.user.username))
    return HttpResponse(data, mimetype='application/json')
