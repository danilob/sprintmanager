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
