from rest_framework import generics
from task.models import Task
from task.api.permissions import IsAdminUserOrReadOnly
from task.api.serializers import TaskSerializer


class ListView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUserOrReadOnly]