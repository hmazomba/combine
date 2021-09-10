
from .views import PostList, PostDetail, PostSearch, PostListDetailFilter
#from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'blog_api'

""" router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls """

""" 
        Alternate method using the url to filter.    
    path('posts/<str:pk>', PostDetail.as_view(), name='detailcreate'), """
    
urlpatterns = [    
    path('posts/', PostDetail.as_view(), name='detailcreate'), 
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]