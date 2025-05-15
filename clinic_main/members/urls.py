from django.urls import path
from .views import register
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.CustomLogoutView.as_view(),name='logout'),
]