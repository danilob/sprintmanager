from django.urls import path

from .views import (
    SprintCreateAPIView,
    SprintRetrieveUpdateDestroyAPIView,
    ListLateSprint,
    CategoriesBySprint,
)

urlpatterns = [
    # api/sprint/
    path(
        route='sprint/',
        view=SprintCreateAPIView.as_view(),
        name='sprint_api',
    ),
    # api/sprint/:uuid/
    path(
        route='sprint/<uuid:uuid>/',
        view=SprintRetrieveUpdateDestroyAPIView.as_view(),
        name='sprint_api',
    ),
    # api/sprint/late/
    path(
        route='sprint/late/',
        view=ListLateSprint.as_view(),
        name='sprint_late_api',
    ),
    # api/sprint/categories/:uuid
    path(
        route='sprint/categories/<uuid:uuid>/',
        view=CategoriesBySprint.as_view(),
        name='sprint_categories_api',
    ),
]
