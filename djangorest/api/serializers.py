from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """map model into json"""

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')