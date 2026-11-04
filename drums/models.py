from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя участника')
    photo = models.ImageField(blank=True, upload_to='participants', verbose_name='Фото участника')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.name


class Payment(models.Model):
    date = models.DateField(verbose_name='Дата платежа')
    amount = models.IntegerField(verbose_name='Сумма платежа')
    participant = models.ForeignKey('Participant', on_delete=models.PROTECT, verbose_name='Участник')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.participant} --- {self.amount} BYN'


class Statement(models.Model):
    image = models.ImageField(verbose_name='Состояние счета', upload_to='statement')

    class Meta:
        verbose_name = 'Состояние счета'
        verbose_name_plural = 'Состояние счета'
