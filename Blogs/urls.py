from django.urls import path,include
from .views import PostCreate,BlogsView
from . import views

urlpatterns = [
    path('create-blogs/',PostCreate.as_view(),name="create-blog"),
    path('',BlogsView.as_view(),name="blogs"),
    path('upvote/',views.upvote,name='upvote')
]