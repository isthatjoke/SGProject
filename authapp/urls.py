from django.urls import path
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.HubUserLoginView.as_view(), name='login'),
    path('logout/', views.HubUserLogoutView.as_view(), name='logout'),
    path('register/', views.HubUserRegisterView.as_view(), name='register'),
    path('user/update/', views.HubUserUpdateView.as_view(), name='update'),
    path('user/update/success/', views.HubUserUpdateView.as_view(), {'success': 'success'}, name='update_success'),
    path('success/', views.Success.as_view(), name='success'),
]



