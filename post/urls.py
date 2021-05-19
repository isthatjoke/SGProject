from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),

    path('user/<int:pk>/posts/', views.ListOfPostsView.as_view(), name='users_posts'),

    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),

    path('myposts/', views.PostUserListView.as_view(), name='users_posts'),
    path('myposts/publish/<int:pk>/', views.post_publish, name='post_publish'),
    path('myposts/archive/<int:pk>/', views.post_archive, name='post_archive'),
    path('myposts/unpublished/<int:pk>/', views.post_restore, name='post_restore'),
    path('myposts/template/<int:pk>/', views.post_template, name='post_template'),
    path('myposts/moderate/<int:pk>/', views.post_moderate, name='post_moderate'),

    path('moderate/', views.PostModerateListView.as_view(), name='post_to_moderate'),
    path('moderate/<int:pk>', views.PostModerateView.as_view(), name='post_moderating'),
    # path('moderate/<int:pk>/', views.post_moderate_done, name='post_moderate_done'),
    # path('moderate/<int:pk>/', views.post_need_review, name='post_need_review'),
    # path('moderate/<int:pk>/', views.post_moderate_false, name='post_moderate_false'),

    path('<int:pk>/karma/<int:pk2>/', views.karma_update, name='karma_update'),
    # path('comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('<int:pk>/comment/update/', views.ajax_comment_update, name='comment_update'),
    path('<int:pk2>/comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/comment/del/<int:comment_id>/', views.ajax_comment_delete, name='del_comment'),
    path('mycomments/', views.CommentUserlist.as_view(), name='comment_list'),
    path('<int:pk>/comment/<int:pk2>/karma/<int:pk3>/', views.comment_karma_update, name='comment_karma_update'),

    path('<int:pk>/comment/<int:comment_id>/complaint/', views.CreateComplaintView.as_view(), name='complaint_create'),
    path('<int:pk>/comment/<int:comment_id>/complaint/<int:complaint_id>/satisfy/', views.satisfy_comment_complaint,
         name='satisfy_comment_complaint'),
    path('<int:pk>/comment/<int:comment_id>/complaint/<int:complaint_id>/dismiss/', views.dismiss_comment_complaint,
         name='dismiss_comment_complaint')
]
