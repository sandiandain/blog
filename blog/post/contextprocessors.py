#coding: utf-8

from post.models import *
from django.db.models import *
def slider_context_processors(request):
    context = {}
    context['category']=Post.objects.values('category','category__name').annotate(count = Count('*'))
    context['archive']=Post.objects.values('created').annotate(count = Count('*')).order_by('-created')
    context['recent']=Post.objects.order_by('-created').all()[:5]

    return context


