from django.urls import path
from . import views
from .views import AdsListView, AdsCreateView, AdsDetailView, AdsUpdateView, AdsDeleteView, UserListView

urlpatterns = [
    path('', AdsListView.as_view(), name='newsfeed-home'),
    path('newsfeed/', AdsListView.as_view(), name='newsfeed-home'),
    path('user/<username>/', UserListView.as_view(), name='user-ads'),
    path('newsfeed/<int:pk>/', AdsDetailView.as_view(), name='ad-detail'),
    path('newsfeed/<int:pk>/update/', AdsUpdateView.as_view(), name='ad-update'),
    path('create-ad/', AdsCreateView.as_view(), name='create-ad'),
    path('newsfeed/<int:pk>/delete/', AdsDeleteView.as_view(), name='ad-delete'),
    path('about/', views.about, name='newsfeed-about')

]
