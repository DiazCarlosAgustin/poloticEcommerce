from django.contrib import admin
from django.urls import path
from django.urls import include


from django.conf.urls.static import static
from django.conf import settings

from . import views
from products.views import ProductIndexListView
urlpatterns = [
    # @url, 
    path('', ProductIndexListView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('productos/', include('products.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)