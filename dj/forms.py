from django import forms
from .models import Entry
import re
import bleach
from django.utils.html import escape



class StihForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['author', 'title', 'txt', 'datepublic']
        labels = {
            'author': 'Ваше ФИО',
            'title': 'Название произведения',
            'txt': 'Текст произведения',
            'datepublic': 'Дата публикации'
        }
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше ФИО',
                'required': True,
                'autocomplete': 'off'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название произведения',
                'required': True,
                'autocomplete': 'off'
            }),
            'txt': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст произведения',
                'rows': 3,
                'required': True,
                'autocomplete': 'off'
            }),
            'datepublic': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
                'autocomplete': 'off'
            })
        }

    def clean_author(self):
        author = self.cleaned_data['author']
        # Экранируем специальные символы
        author = escape(author)
        # Очищаем от HTML/JavaScript
        author = bleach.clean(author, strip=True)
        
        if len(author) < 2:
            raise forms.ValidationError('ФИО должно содержать минимум 2 символа')
        if not re.match(r'^[а-яА-ЯёЁ\s-]+$', author):
            raise forms.ValidationError('ФИО должно содержать только русские буквы, пробелы и дефисы')
        return author

    def clean_title(self):
        title = self.cleaned_data['title']
        # Экранируем специальные символы
        title = escape(title)
        # Очищаем от HTML/JavaScript
        title = bleach.clean(title, strip=True)
        
        if len(title) < 2:
            raise forms.ValidationError('Название должно содержать минимум 2 символа')
        if len(title) > 40:
            raise forms.ValidationError('Название не должно превышать 40 символов')
        if not re.match(r'^[а-яА-ЯёЁ\s-]+$', title):
            raise forms.ValidationError('Название должно содержать только русские буквы, пробелы и дефисы')
        return title

    def clean_txt(self):
        txt = self.cleaned_data['txt']
        # Экранируем специальные символы
        txt = escape(txt)
        # Очищаем от HTML/JavaScript
        txt = bleach.clean(txt, strip=True)
        
        if len(txt) < 10:
            raise forms.ValidationError('Текст стихотворения должен содержать минимум 10 символов')
        if len(txt) > 1000:
            raise forms.ValidationError('Текст стихотворения не должен превышать 1000 символов')
        # Проверяем, что текст содержит хотя бы одну строку с рифмой (минимум 2 строки)
        lines = txt.split('\n')
        if len(lines) < 2:
            raise forms.ValidationError('Стихотворение должно содержать минимум 2 строки')
        return txt

    def clean_datepublic(self):
        datepublic = self.cleaned_data['datepublic']
        from datetime import date
        if datepublic > date.today():
            raise forms.ValidationError('Дата публикации не может быть в будущем')
        return datepublic
