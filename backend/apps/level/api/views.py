# flavors/api/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.permissions import IsAuthenticated
from ..models import Level
from .serializers import LevelSerializer


class LevelCreateAPIView(ListCreateAPIView):
    queryset = Level.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = LevelSerializer


class LevelRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = LevelSerializer
