from django.urls import path
from .views import PostViewSet, CommentViewSet, FeedView, LikeViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

like_list = LikeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

like_detail = LikeViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('', post_list, name='post-list'),  # Adjusted to have the 'posts/' prefix
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
    path('comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>/', comment_detail, name='comment-detail'),
    path('likes/', like_list, name='like-list'),
    path('likes/<int:pk>/', like_detail, name='like-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
]