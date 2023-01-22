# flavors/api/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.permissions import IsAuthenticated
from ..models import Sprint
from .serializers import SprintSerializer


class SprintCreateAPIView(ListCreateAPIView):
    queryset = Sprint.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = SprintSerializer
    lookup_field = 'uuid'  # Don't use Sprint.id!


class SprintRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sprint.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = SprintSerializer
    lookup_field = 'uuid'  # Don't use Sprint.id!


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status


class ListLateSprint(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        sprints_late = Sprint.sprint_delivered_late()
        serializer = SprintSerializer(sprints_late, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CategoriesBySprint(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, uuid, format=None):
        issues_categories = Sprint.objects.get(uuid=uuid).sumarize_categories_count()
        return Response(issues_categories, status.HTTP_200_OK)


class SprintChartJson(APIView):
    def get(self, request, format=None):
        from apps.issue.models import Issue
        from django.db.models import F
        dataset_all = Issue.objects.annotate(sprint_uuid=F("sprint__uuid"),sprint_description=F("sprint__description"),category=F("categories__description")).values("sprint_uuid","sprint_description","uuid","category")
        return Response(dataset_all, status.HTTP_200_OK)