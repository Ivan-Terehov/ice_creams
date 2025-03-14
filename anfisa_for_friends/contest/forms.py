from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label="Название",
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5},
    ))
    price = forms.IntegerField(
        label='Цена',
        min_value=10,
        max_value=100,
        help_text='Рекомендованная розничная цена',
    )
    comment = forms.CharField(
        label="Комментарий",
        required=False,
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5},
    ))