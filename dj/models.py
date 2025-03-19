from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.html import escape
import bleach


class xd(models.Model):
    nazv=models.TextField(max_length=10000)
    txt=models.TextField(max_length=10000)
    def __str__(self):
        return self.nazv


class xd2(models.Model):
    nazv2 = models.TextField(max_length=10000)
    txt2 = models.TextField(max_length=10000)
    aut2 = models.TextField(max_length=10000)
    def __str__(self):
        return self.nazv2


class xd3(models.Model):
    nazv3 = models.TextField(max_length=10000)
    txt3 = models.TextField(max_length=10000)
    def __str__(self):
        return self.nazv3


class xd4(models.Model):
    nazv4=models.TextField(max_length=10000)
    txt4=models.TextField(max_length=10000)
    def __str__(self):
        return self.nazv4


class Entry(models.Model):
    author = models.TextField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁ\s-]+$',
                message='ФИО должно содержать только русские буквы, пробелы и дефисы'
            )
        ]
    )
    title = models.TextField(
        max_length=40,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁ\s-]+$',
                message='Название должно содержать только русские буквы, пробелы и дефисы'
            )
        ]
    )
    txt = models.TextField(max_length=1000)
    datepublic = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries', null=True, blank=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

    def save(self, *args, **kwargs):
        # Очищаем данные от потенциально опасного HTML/JavaScript
        self.author = bleach.clean(self.author, strip=True)
        self.title = bleach.clean(self.title, strip=True)
        self.txt = bleach.clean(self.txt, strip=True)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'entry'
        indexes = [
            models.Index(fields=['author']),
            models.Index(fields=['datepublic']),
        ]




