from rest_framework import serializers
from .models import College, CollegeMedia, CollegeInfo

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class CollegeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeMedia
        fields = '__all__'


class CollegeInfoSerializer(serializers.ModelSerializer):
    college = CollegeSerializer()
    college_media = CollegeMediaSerializer(many=True)

    class Meta:
        model = CollegeInfo
        fields = '__all__'
