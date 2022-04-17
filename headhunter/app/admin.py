from django.contrib import admin
from app.models import (
    Summary, WorkExperience,
    Education, Response,
    Message
)


class SummaryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'username', 'summary_position', 'category', 'salary', 'phone_number',
        'email', 'telegram', 'facebook', 'linkedin', 'publication', 'updated_at'
    ]


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = [
       'id', 'user', 'company_name', 'work_position', 'responsibilities', 'start_work', 'finish_work'
    ]


class EducationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'educational_center', 'speciality', 'start_education', 'finish_education'
    ]


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'applicant', 'employer', 'summary', 'vacancy']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'response', 'created_at']


admin.site.register(Summary, SummaryAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Message, MessageAdmin)
