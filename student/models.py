from django.db import models


class Dishes(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    composition = models.TextField(blank=False, null=True, verbose_name='Состав')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    food_intake = models.CharField(max_length=150, verbose_name='Приём пищи')

    class Meta:
        db_table = 'dishes'
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ("id", )

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"
    
    def display_composition(self):
        return self.composition.replace("|", ", ")
    
    def display_subscription_price(self):
        return f"{self.price*8/10}"