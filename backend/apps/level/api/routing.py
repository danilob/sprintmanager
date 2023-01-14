from django.urls import path

from .views import LevelCreateAPIView, LevelRetrieveUpdateDestroyAPIView

urlpatterns = [
    # api/level/
    path(
        route='level/',
        view=LevelCreateAPIView.as_view(),
        name='level_api',
    ),
    # api/level/:uuid/
    path(
        route='level/<int:pk>/',
        view=LevelRetrieveUpdateDestroyAPIView.as_view(),
        name='level_api',
    ),
]
