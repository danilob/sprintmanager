from django.urls import path

from .views import SprintCreateAPIView, SprintRetrieveUpdateDestroyAPIView

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
]
