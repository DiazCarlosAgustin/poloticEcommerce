from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # @url, 
    path('admin/', admin.site.urls),
    path('', views.index, name="index")
]
