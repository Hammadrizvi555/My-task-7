from django.urls import path
from Blog_API.views import (
    RegisterView,
    LoginView,  # Changed from CustomAuthToken
    PostListView,  # Changed from PostListCreateView
    PostDetailView,  # Changed from PostRetrieveUpdateDestroyView
    CommentListView,  # Changed from CommentListCreateView
    CommentDetailView  # Changed from CommentRetrieveDestroyView
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  # Changed to LoginView
    
    # Posts
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Comments
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]