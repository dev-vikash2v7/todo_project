from rest_framework import serializers
from .models import ToDo, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ToDoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'due_date', 'tags', 'status', 'timestamp']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo = ToDo.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            todo.tags.add(tag)
        return todo

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)
        return instance
