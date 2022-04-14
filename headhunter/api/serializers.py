from rest_framework import serializers
from app.models import WorkExperience, Education


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = [
            'id', 'user', 'company_name',
            'work_position', 'responsibilities', 'start_work', 'finish_work'
        ]
        read_only_fields = ['id', 'user']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id', 'user', 'educational_center',
            'speciality', 'start_education', 'finish_education'
        ]
        read_only_fields = ['id', 'user']
