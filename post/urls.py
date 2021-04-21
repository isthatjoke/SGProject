from django.urls import path
from post import views

app_name = 'post'


urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),

    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),

    path('myposts/', views.PostUserListView.as_view(), name='users_posts'),
    path('myposts/publish/<int:pk>/', views.post_publish, name='post_publish'),
    path('myposts/archive/<int:pk>/', views.post_archive, name='post_archive'),
    path('myposts/unpublished/<int:pk>/', views.post_restore, name='post_restore'),
    path('myposts/template/<int:pk>', views.post_template, name='post_template'),

    path('<int:pk>/karma/<int:pk2>/', views.karma_update, name='karma_update'),
    path('comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('<int:pk2>/comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('mycomments/', views.CommentUserlist.as_view(), name='comment_list'),
    path('<int:pk>/comment/<int:pk2>/karma/<int:pk3>/', views.comment_karma_update, name='comment_karma_update'),
]





