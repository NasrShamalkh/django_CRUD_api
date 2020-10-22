from .models import Post
from rest_framework.serializers import ModelSerializer
# Here we create our Posts serializers to handle DATABASE


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'published',
            'likes'
        )

