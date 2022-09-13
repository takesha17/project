from django.urls import path

from .views import hello,posts,post_detail


urlpatterns = [
    path('hello/', hello),
    path('posts/',posts),
    path('post/<int:id>/', post_detail)
]
