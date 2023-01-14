# flavors/api/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.permissions import IsAuthenticated
from ..models import Issue
from .serializers import IssueSerializer


class IssueCreateAPIView(ListCreateAPIView):
    queryset = Issue.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = IssueSerializer
    lookup_field = 'uuid'  # Don't use Issue.id!


class IssueRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = IssueSerializer
    lookup_field = 'uuid'  # Don't use Issue.id!
