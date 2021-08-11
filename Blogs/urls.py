from django.urls import path,include
from .views import PostCreate,BlogsView,upvote,comment
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-blogs/',PostCreate.as_view(),name="create-blog"),
    path('',BlogsView.as_view(),name="blogs"),
    # path('upvote/',views.upvote,name='upvote')
    path('upvote/',upvote.as_view(),name='upvote'),
    path('comment/',comment.as_view(),name='comment'),

]
