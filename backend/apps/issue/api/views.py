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


from .serializers import IssueCustomSerializer
from rest_framework.generics import ListCreateAPIView


class IssueCustomDurationList(ListCreateAPIView):
    queryset = Issue.issues_classified_by_max_duration()
    serializer_class = IssueCustomSerializer


from .serializers import IssueCustomDurationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def custom_duration_issue(request):
    from django.db.models import F
    from django.db.models.functions import ExtractDay

    issues = (
        Issue.objects.filter(status=Issue.DONE)
        .annotate(sprint_name=F('sprint__description'))
        .annotate(days=ExtractDay(F('finished_date') - F('begin_date')))
        .values('sprint_name', 'description', 'days')
        .order_by('-days')
    )
    serializer = IssueCustomDurationSerializer(issues, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
