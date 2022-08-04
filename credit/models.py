from django.db import models
#
#
# def year(self):
#     return self.birth_year.strftime('%Y')


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО')
    citizenship = models.CharField(max_length=20, default='Кыргызстан', verbose_name='Гражданство')
    birth_year = models.DateField(verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, null=True, blank=True, verbose_name='Место работы')
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'



class Account(models.Model):
    number = models.CharField(max_length=16, unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, blank=True, verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        db_table = 'accounts'


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата получения кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Счет')

    def __str__(self):
        return self.sum

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
        db_table = 'loans'
