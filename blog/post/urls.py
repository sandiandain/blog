
#coding: utf-8


from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^page/(\d+)$',views.index),
    url(r'^post/details/(\d+)$',views.post_details_view),
    url(r'^category/(\d+)$',views.category_details_view),
    url(r'^archive/(\d+)/(\d+)/(\d+)$',views.date_details_view),
    url(r'^search/$',views.search_view),
]