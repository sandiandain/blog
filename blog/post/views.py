from django.shortcuts import render
from post.models import *
from django.views.generic import ListView
# Create your views here.
# class index(ListView):
#     template_name = 'index.html'
#     model = Post
#     context_object_name = 'post_obj'

def index(request,num = '1'):
    page,page_range= Post.get_posts_by_page(num,4)
    return render(request,'index.html',context={'page':page,'page_range':page_range})


def post_details_view(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except:
        pass

    return render(request,'details.html',{'post':post})


def category_details_view(request,category_id=None):
    posts = Post.objects.filter(category=category_id).order_by('-created')
    return render(request,'archive.html',{'posts':posts})


def date_details_view(request,year,month,day):
    posts = Post.objects.filter(created__year=year,created__month=month,created__day=day).all()
    return render(request,'archive.html',{'posts':posts})



def search_view(request):
    keyword = request.GET.get('q')
    # model层也是这样操作的
    from  django.core.paginator import Paginator
    from haystack.query import SearchQuerySet
    # from django.db.models import Q
    from haystack.query import SQ
    paginator = Paginator(SearchQuerySet().filter(SQ(title = keyword)|SQ(content = keyword)).all(), 10)
    page = paginator.page(1)
    posts = []

    for result in page.object_list:
        posts.append(result.object)
    return render(request,'archive.html',{'posts':posts})