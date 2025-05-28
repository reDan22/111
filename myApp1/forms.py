import re
from django import forms
from .models import PCConfiguration


class PCConfigForm(forms.ModelForm):
    email = forms.CharField(
        label='Email*',
        widget=forms.TextInput(attrs={
            'placeholder': 'example@domain.com',
            'autocomplete': 'off'
        })
    )
    phone = forms.CharField(
        label='Телефон*',
        widget=forms.TextInput(attrs={
            'placeholder': '+79991234567',
            'autocomplete': 'off'
        })
    )
    customer_name = forms.CharField(
        label='ФИО*',
        widget=forms.TextInput(attrs={
            'placeholder': 'Иванов Иван Иванович',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = PCConfiguration
        fields = ['customer_name', 'email', 'phone', 'cpu', 'gpu', 'ram', 'ssd']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['cpu', 'gpu', 'ram', 'ssd']:
            self.fields[field_name].label_from_instance = lambda obj: f"{obj.name} ({obj.price} руб.)"
            self.fields[field_name].widget.attrs.update({'class': 'form-select'})

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-3',
                'autocomplete': 'off',
                'required': False,  # отключаем HTML5-валидацию
                'type': 'text'      # убираем тип "email", чтобы не было нативной проверки
            })

    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name')
        if not re.match(r'^[А-ЯЁ][а-яё]+(?:\s[А-ЯЁ][а-яё]+){1,2}$', name):
            raise forms.ValidationError(
                'ФИО должно быть в формате: Фамилия Имя Отчество. Только русские буквы, с заглавных.'
            )
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            raise forms.ValidationError("Введите корректный email адрес.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        cleaned_phone = re.sub(r"[^\d+]", "", phone)

        if cleaned_phone.startswith("+7"):
            if not re.match(r"^\+7\d{10}$", cleaned_phone):
                raise forms.ValidationError('Номер должен быть в формате +7XXXXXXXXXX.')
            return cleaned_phone
        elif cleaned_phone.startswith("8"):
            if not re.match(r"^8\d{10}$", cleaned_phone):
                raise forms.ValidationError('Номер должен быть в формате 8XXXXXXXXXX.')
            return cleaned_phone
        else:
            raise forms.ValidationError(
                'Телефон должен начинаться с +7 или 8 и содержать 11 цифр.'
            )
