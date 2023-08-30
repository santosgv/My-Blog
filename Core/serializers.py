from rest_framework import serializers
from Core.models import Post

class PostSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'