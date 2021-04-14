from django.urls import path
from post import views

app_name = 'post'


urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('myposts/', views.PostUserListView.as_view(), name='users_posts'),
    path('<int:pk>/karma/<int:pk2>/', views.karma_update, name='karma_update'),
]




