from django.urls import path

from . import views
app_name = 'verifications'


urlpatterns = [
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('register/',views.Register.as_view(),name='register'),
    path('logout/',views.logout,name='logout')
]
