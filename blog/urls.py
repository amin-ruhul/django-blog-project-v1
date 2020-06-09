from django.urls import path

from . import views
from . views import BlogCreateView,BlogUpdate,Blogdetails,BlogList,BlogDelete
urlpatterns = [
    
    path('', BlogList.as_view(), name = 'index'),
    path('post/<int:pk>/',Blogdetails.as_view(),name='post'),
    path('post/new/', BlogCreateView.as_view(),name = 'new_post'),
    path('post/<int:pk>/edit/',BlogUpdate.as_view(),name='edit_post'),
    path('post/<int:pk>/delete/',BlogDelete.as_view(),name='delete_post')
]