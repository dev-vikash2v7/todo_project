from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer

from django.views.generic import ListView


class ToDoCreateView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetailView(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoUpdateView(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDeleteView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
