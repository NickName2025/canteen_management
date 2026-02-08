from django.db import models

from users.models import User


class DishesServed(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    dish_name = models.CharField(verbose_name='Блюдо')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'dishes_served'
        verbose_name = 'Выданное блюдо'
        verbose_name_plural = 'выданные блюда'
        ordering = ("id", )

    def __str__(self):
        return f'{self.user.username} | Блюдо {self.dish_name}'
    

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    units_of_measurement = models.CharField(verbose_name='Еденицы измерения')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id", )

    def __str__(self):
        return f"{self.name} Количество - {self.quantity} {self.units_of_measurement}"
    
    def get_list_of_possible_products(self):
        return [("мука пшеничная", "кг"), ("вода", "л"), ("сахар", "кг"), ("растительное масло", "л"), ("сливочное масло", "г")]