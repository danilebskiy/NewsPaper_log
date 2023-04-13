from django.urls import path

from news.views import PostList

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
]