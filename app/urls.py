from django.urls import path
from .views import index, region_detail, user_login, user_logout, user_register, about_us

urlpatterns = [
    path('', index, name="index"),
    path('selected-info/<int:pk>/', region_detail, name="region_detail"),
    path('about/', about_us, name="about"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('register/', user_register, name="register"),
]
