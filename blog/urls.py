from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post'),
]
