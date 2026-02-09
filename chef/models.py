from django.db import models

from users.models import User


class DishesServed(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    dish_name = models.CharField(max_length=150, verbose_name='Блюдо')
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
    units_of_measurement = models.CharField(max_length=150, verbose_name='Еденицы измерения')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id", )

    def __str__(self):
        return f"{self.name} Количество - {self.quantity} {self.units_of_measurement}"
    

class PurchaseRequests(models.Model):
    products_names = models.TextField(verbose_name='Названия продуктов')
    products_quantity = models.TextField(verbose_name='Количество продуктов')
    units_of_measurement = models.TextField(max_length=150,verbose_name='Еденицы измерения')
    status = models.BooleanField(default=False, verbose_name='Статус (принято)')
    rejected = models.BooleanField(default=False, verbose_name='Отклонено')
    in_process_of_adding = models.BooleanField(default=False, verbose_name='В процессе добавления')

    class Meta:
        db_table = 'purchase_requests'
        verbose_name = 'Заявка на покупку'
        verbose_name_plural = 'Заявки на покупку'
        ordering = ("id", )
    
    def __str__(self):
        return f"Статус: {self.status} Отклонено: {self.rejected} В процессе джобавления: {self.in_process_of_adding}"
    
    def get_list(self):
        list = []

        list_of_products_names = self.products_names.split("|")[:-1]
        list_of_products_quantity = self.products_quantity.split("|")[:-1]
        list_of_units_of_measurement = self.units_of_measurement.split("|")[:-1]
        
        for i in range(len(list_of_products_names)):
             list.append((
                 list_of_products_names[i],
                 list_of_products_quantity[i],
                 list_of_units_of_measurement[i]
             ))

        return list