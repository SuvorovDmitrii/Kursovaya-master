from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Types (models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование категории")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


"""class Role (models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование роли")

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'"""


class Person (models.Model):
    #role = models.ForeignKey( 'Role', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, verbose_name="Отчество", blank=True, null=True)
    number = models.IntegerField(verbose_name="Номер")
    user = models.OneToOneField( User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Request (models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    type = models.ForeignKey('Types', on_delete=models.CASCADE, verbose_name="Категория запроса")
    datetime = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, verbose_name="Текст запроса")
    img = models.ImageField(verbose_name="Фото", null=True, blank=True, upload_to='images/', default='default.jpg')
    on_del = models.BooleanField(verbose_name="Статус удаления пользователем", default=False)


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-datetime']


class Status (models.Model):
    request = models.ForeignKey('Request', on_delete=models.CASCADE, verbose_name='Заявка',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',)
    category = models.ForeignKey('Category', verbose_name='Тип статуса', on_delete=models.CASCADE, default='0')
    type = models.ForeignKey('Types', verbose_name='Категория', on_delete=models.SET_DEFAULT, default='0')
    datetime = models.DateTimeField(default=timezone.now, verbose_name='Время запроса')
    text = models.CharField(max_length=200, verbose_name="Описание статуса")

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Статус")

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name
