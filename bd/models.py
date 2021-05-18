from django.db import models


class ClickStatistics(models.Model):
    time = models.CharField('ДатаВремя', max_length=250)
    f_name = models.CharField('Выполненая функции', max_length=250)
    user_id = models.CharField('User id', max_length=250)
    user_name = models.CharField('User name', max_length=250)
    user_fullname = models.CharField('User fullname', max_length=250)

    def __str__(self):
        return f'{self.time}; Выполнена функция: "{self.f_name}"; ID пользователя: {self.user_id}'

    class Meta:
        verbose_name = 'Статистика действий пользователей'
        verbose_name_plural = 'Статистика действий пользователей'


class UserRequests(models.Model):
    user_id = models.CharField('User id', max_length=250)
    user_name = models.CharField('User name', max_length=250)
    user_fullname = models.CharField('User fullname', max_length=250)
    time = models.CharField('ДатаВремя', max_length=250)

    def __str__(self):
        return f'Пользователь {self.user_fullname}(@{self.user_name}), назначил(а) встречу на: {self.time}'

    class Meta:
        verbose_name = 'Запланированные встречи администратора и пользователей'
        verbose_name_plural = 'Запланированные встречи администратора и пользователей'

