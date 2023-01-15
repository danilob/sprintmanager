# flavors/api/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.permissions import IsAuthenticated
from ..models import Category
from .serializers import CategorySerializer


class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer
    lookup_field = 'uuid'  # Don't use Category.id!


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer
    lookup_field = 'uuid'  # Don't use Category.id!
