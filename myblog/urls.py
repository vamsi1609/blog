from django.urls import path
from .views import HomeView, ArticleView, AddPost, UpdatePost
from .views import DeletePost, AddCategory

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add/', AddPost.as_view(), name='add_post'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/remove/<int:pk>', DeletePost.as_view(), name='delete_post'),
]
