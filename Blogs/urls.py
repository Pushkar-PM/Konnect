from django.urls import path,include
from .views import PostCreate,BlogsView,upvote,Blog_global
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-blogs/',PostCreate.as_view(),name="create-blog"),
    path('',BlogsView.as_view(),name="blogs"),
    # path('upvote/',views.upvote,name='upvote')
    path('upvote/',upvote.as_view(),name='upvote'),
    path('addcomment/', views.addcomment, name='addcomment'),
    path('global/',Blog_global.as_view(),name='global'),
]
