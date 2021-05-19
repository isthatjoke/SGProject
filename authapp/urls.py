from django.urls import path
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.HubUserLoginView.as_view(), name='login'),
    path('logout/', views.HubUserLogoutView.as_view(), name='logout'),
    path('register/', views.HubUserRegisterView.as_view(), name='register'),
    path('update/', views.HubUserUpdateView.as_view(), name='update'),
    path('success/', views.Success.as_view(), name='success'),
    path('users_rating/', views.UsersRatingListView.as_view(), name='users_rating'),
]



