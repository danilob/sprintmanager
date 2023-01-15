from django.urls import path

from .views import CategoryCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    # api/category/
    path(
        route='category/',
        view=CategoryCreateAPIView.as_view(),
        name='category_api',
    ),
    # api/category/:uuid/
    path(
        route='category/<uuid:uuid>/',
        view=CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name='category_api',
    ),
]
