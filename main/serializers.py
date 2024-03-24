from django.urls import reverse
from rest_framework import serializers

from .models import GenericTemplate


class GenericTemplateSerializer(serializers.ModelSerializer):
    file_upload_url = serializers.SerializerMethodField()
    image_preview_url = serializers.SerializerMethodField()

    class Meta:
        model = GenericTemplate
        fields = "__all__"

    def get_file_upload_url(self, obj):
        if obj.file_upload:
            return obj.file_upload.url
        return None

    def get_image_preview_url(self, obj):
        if obj.image_preview:
            return obj.image_preview.url
        return None
