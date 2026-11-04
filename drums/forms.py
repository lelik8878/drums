from django import forms
from .models import Participant


class AddParticipantForm(forms.Form):
    name = forms.CharField(label='Имя участника')
    photo = forms.ImageField(label='Фото участника', required=False)


class AddPaymentForm(forms.Form):
    date = forms.DateField(label='Дата', widget=forms.DateInput(format='%Y-%m-%d',
                                                                attrs={"type": "date", "class": "form-control"}))
    amount = forms.IntegerField(label='Количество')
    participant = forms.ModelChoiceField(label='Участник', queryset=Participant.objects)


class AddStatementForm(forms.Form):
    image = forms.ImageField(label='Состояние счета')
