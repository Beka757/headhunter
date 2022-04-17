from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


CATEGORY_VACANCY = [
    ('Information technology', 'Информационные технологии'),
    ('Medicine', 'Медецина'),
    ('Marketing', 'Маркетинг'),
    ('Sales', 'Продажи'),
    ('Production', 'Производство'),
    ('Insurance', 'Страхование')
]


class Summary(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='summary_user', verbose_name='Пользователь'
    )
    username = models.CharField(max_length=150, verbose_name='Имя')
    summary_position = models.CharField(max_length=100, verbose_name='Должность')
    category = models.CharField(max_length=50, choices=CATEGORY_VACANCY, verbose_name='Категория вакансии')
    salary = models.IntegerField(
        validators=[MaxValueValidator(1000000), MinValueValidator(1)],
        verbose_name='Заработная плата'
    )
    phone_number = PhoneNumberField(region='KZ', verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    telegram = models.URLField(max_length=500, verbose_name='Telegram')
    facebook = models.URLField(max_length=500, null=True, blank=True, verbose_name='Facebook')
    linkedin = models.URLField(max_length=500, null=True, blank=True, verbose_name='Linkedin')
    work_experience = models.ManyToManyField('app.WorkExperience', related_name='summary_experience', blank=True)
    education = models.ManyToManyField('app.Education', related_name='summary_education', blank=True)
    publication = models.BooleanField(verbose_name='Публикация резюме')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.summary_position


class WorkExperience(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='work_user', verbose_name='Пользователь'
    )
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    work_position = models.CharField(max_length=100, verbose_name='Должность')
    responsibilities = models.TextField(max_length=3000, verbose_name='Обязанности')
    start_work = models.DateField(verbose_name='Дата начала')
    finish_work = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    def __str__(self):
        return self.work_position


class Education(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='education_user', verbose_name='Пользователь'
    )
    educational_center = models.CharField(max_length=100, verbose_name='Образовательный центр')
    speciality = models.CharField(max_length=100, verbose_name='Специальность')
    start_education = models.DateField(verbose_name='Дата начала')
    finish_education = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    def __str__(self):
        return self.speciality


class Vacancy(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='vacancy_user', verbose_name='Пользователь'
    )
    vacancy_position = models.CharField(max_length=100, verbose_name='Должность')
    category = models.CharField(max_length=50, choices=CATEGORY_VACANCY, verbose_name='Категория вакансии')
    salary = models.IntegerField(
        validators=[MaxValueValidator(1000000), MinValueValidator(1)],
        verbose_name='Заработная плата'
    )
    description = models.TextField(max_length=3000, verbose_name='Описание вакансии')
    work_experience_from = models.IntegerField(
        validators=[MaxValueValidator(9), MinValueValidator(0)],
        verbose_name='Заработная плата от'
    )
    work_experience_to = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)],
        verbose_name='Заработная плата до'
    )
    publication = models.BooleanField(verbose_name='Публикация вакансии')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


class Response(models.Model):
    applicant = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name="responses_applicant", verbose_name='Соискатель'
    )
    employer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name="responses_employer", verbose_name='Работадатель'
    )
    summary = models.ForeignKey(
        Summary, on_delete=models.CASCADE,
        related_name="responses_summary", verbose_name='Резюме'
    )
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE,
        related_name="responses_vacancy", verbose_name='Вакансия'
    )
    
    
class Message(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name="messages_user", verbose_name='Пользователь'
    )
    response = models.ForeignKey(
        Response, on_delete=models.CASCADE,
        related_name="messeges_response", verbose_name='Отклик'
    )
    text = models.TextField(max_length=3000, verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

