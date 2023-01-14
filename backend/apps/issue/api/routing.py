from django.urls import path

from .views import IssueCreateAPIView, IssueRetrieveUpdateDestroyAPIView

urlpatterns = [
    # api/category/
    path(
        route='issue/',
        view=IssueCreateAPIView.as_view(),
        name='issue_api',
    ),
    # api/issue/:uuid/
    path(
        route='issue/<uuid:uuid>/',
        view=IssueRetrieveUpdateDestroyAPIView.as_view(),
        name='issue_api',
    ),
]
