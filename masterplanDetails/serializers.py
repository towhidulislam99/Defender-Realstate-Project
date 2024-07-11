from rest_framework import serializers
import re
from .models import MasterplanDetails, GalleryImage

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']

class MasterplanDetailsSerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True, read_only=True)
    gallery_images_upload = serializers.ListField(
        child=serializers.ImageField(write_only=True),
        write_only=True
    )

    class Meta:
        model = MasterplanDetails
        fields = ['id', 'project', 'masterplan', 'facilities', 'youtube_url', 'image_floorplan', 'floorplan_pdf', 'gallery_images', 'gallery_images_upload']

    def create(self, validated_data):
        gallery_images_data = validated_data.pop('gallery_images_upload')
        masterplan_detail = MasterplanDetails.objects.create(**validated_data)
        for image_data in gallery_images_data:
            GalleryImage.objects.create(masterplan_detail=masterplan_detail, image=image_data)
        return masterplan_detail

    def update(self, instance, validated_data):
        gallery_images_data = validated_data.pop('gallery_images_upload', None)
        if gallery_images_data:
            GalleryImage.objects.filter(masterplan_detail=instance).delete()
            for image_data in gallery_images_data:
                GalleryImage.objects.create(masterplan_detail=instance, image=image_data)
        return super().update(instance, validated_data)
    
    
    def validate_youtube_url(self, value):
        youtube_regex = (
            r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        if not re.match(youtube_regex, value):
            raise serializers.ValidationError("Enter a valid YouTube URL.")
        return value