from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('frontend.urls')),
]

from django.contrib.auth.models import User

# from rest_framework import routers  # , serializers, viewsets

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

from apps.category.api import routing as routing_category
from apps.level.api import routing as routing_level
from apps.issue.api import routing as routing_issue
from apps.sprint.api import routing as routing_sprint

urlpatterns_api = [
    # path('', include(router.urls)),
    path('api/', include(routing_category)),
    path('api/', include(routing_level)),
    path('api/', include(routing_issue)),
    path('api/', include(routing_sprint)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += urlpatterns_api

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Dummy API",
        default_version='v1',
        description="Dummy description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dummy.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns_doc = [
    path(
        'playground/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'docs/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]

urlpatterns += urlpatterns_doc
