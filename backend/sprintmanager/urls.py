from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns_api = [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += urlpatterns_api
