from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist
from rest_framework import permissions
from .permission import IsOwner
# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """creates the bucketlist"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner) 

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner) 

