from django.urls import path
from . import views
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post', views.PostCreateView.as_view(), name='add_post'),
    path('edit_post/<int:pk>', views.PostUpdateView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.PostDeleteView.as_view(), name='delete_post'),
    ]
