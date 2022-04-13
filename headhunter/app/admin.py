from django.contrib import admin
from app.models import Summary, WorkExperience, Education, SummaryWorkExperience, SummaryEducation


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


class SummaryWorkExperienceAdmin(admin.ModelAdmin):
    exclude = []


class SummaryEducationAdmin(admin.ModelAdmin):
    exclude = []


admin.site.register(Summary, SummaryAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(SummaryWorkExperience, SummaryWorkExperienceAdmin)
admin.site.register(SummaryEducation, SummaryEducationAdmin)
