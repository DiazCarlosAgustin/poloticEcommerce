from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # @url, 
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
]
