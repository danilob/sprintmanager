from django.urls import path

from .views import (
    IssueCreateAPIView,
    IssueRetrieveUpdateDestroyAPIView,
    IssueCustomDurationList,
    custom_duration_issue,
)

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
    # api/issue/duration/
    path(
        route='issue/duration/',
        view=IssueCustomDurationList.as_view(),
        name='issue_duration_api',
    ),
    # api/issue/duration/short/
    path(
        route='issue/duration/short/',
        view=custom_duration_issue,
        name='issue_duration_custom_api',
    ),
]
