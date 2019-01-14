from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
app_name = 'board2'
urlpatterns = [
    path('', PostListView.as_view(), name='postList'),
    path('<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    path('create/',  PostCreateView.as_view(), name="postCreate"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name="postUpdate"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='postDelte' ),
]