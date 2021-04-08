from django.urls import path

from hub import views
app_name = 'hub'

urlpatterns = [
    path('', views.main, name='main'),
    path('category/<int:pk>', views.HubCategoryPostListView.as_view(), name='hub_category'),

]




