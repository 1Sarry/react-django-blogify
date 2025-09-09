from rest_framework import serializers
from .models import Post, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', required=False, write_only=True
    )
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, source='tags', required=False, write_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'author',
            'category', 'category_id',
            'tags', 'tag_ids',
            'status', 'created_at', 'updated_at'
        ]
