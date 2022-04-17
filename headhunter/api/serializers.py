from rest_framework import serializers
from app.models import WorkExperience, Education, Vacancy, Summary, Message


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


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'vacancy_position', 'updated_at'
        ]


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = [
            'summary_position', 'updated_at'
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'response', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']


class VacancyPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['publication']


class SummaryPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['publication']

