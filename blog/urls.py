from django.urls import path

from .views import PostAPIView,PostDetailAPIView


urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view())
]
