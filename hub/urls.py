from django.urls import path

from hub import views
app_name = 'hub'

urlpatterns = [
    path('', views.main, name='main'),
    path('hub/<int:pk>', views.HubPostListView.as_view(), name='hub'),
    path('hub/<int:pk>/category/<int:cat>', views.HubCategoryPostListView.as_view(), name='hub_category'),

]




