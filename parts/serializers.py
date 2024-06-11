from rest_framework import serializers

from parts.models import Part


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = "__all__"
        read_only_fields = ["id"]


class TopWordsSerializer(serializers.Serializer):
    words = serializers.ListField(child=serializers.CharField())
