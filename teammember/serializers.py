from rest_framework import serializers
from .models import TeamMember,AboutUs, VideoAboutUs, CeoAboutUs


#This is About Us  Serializers its same Page About Us
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title_one', 'title_two', 'description', 'image']
        

class VideoAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAboutUs
        fields = ['id', 'title_one', 'title_two', 'description', 'image']
        

class CeoAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CeoAboutUs
        fields = ['id', 'title_one', 'title_two', 'description', 'image']
        
        
#This is Team Member Serializers
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            'id', 'position', 'name', 'description', 'image', 'phone_number', 'email',
            'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link', 'dribble_link'
        ]


