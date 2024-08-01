from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate, BlogReview, BlogSubsc, like_view, dislike_view

urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='update'),
    path('review/<int:pk>/', BlogReview.as_view(), name='review'),
    path('subsc/<int:pk>/', BlogSubsc.as_view(), name='subsc'),
    path('like/<int:pk>/', like_view, name='like'),
    path('dislike/<int:pk>/', dislike_view, name='dislike'),
]