from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type = models.CharField(max_length=150, verbose_name='Тип пользователя')

    intolerant_of_glucose = models.BooleanField(default=False, verbose_name="Непереносит глюкозу")
    intolerant_of_lactose = models.BooleanField(default=False, verbose_name="Непереносит лактозу")
    intolerant_of_sugar = models.BooleanField(default=False, verbose_name="Непереносит сахару")
    intolerant_of_vegetarian = models.BooleanField(default=False, verbose_name="Предпочитает вегетарианское")

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        ordering = ("id", )

    def __str__(self):
        return self.username