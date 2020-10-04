from rest_framework import serializers

from ghostpost.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'post',
            'text',
            'post_date',
            'upvotes',
            'downvotes'

        ]
