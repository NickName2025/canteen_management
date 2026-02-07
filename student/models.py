from django.db import models


class Dishes(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    food_intake = models.CharField(max_length=150, verbose_name='Приём пищи')

    is_glucose = models.BooleanField(verbose_name="Есть глюкоза")
    is_lactose = models.BooleanField(verbose_name="Есть лактоза")
    is_sugar = models.BooleanField(verbose_name="Есть сахара")
    is_vegetarian = models.BooleanField(verbose_name="Вегетарианское")

    class Meta:
        db_table = 'dishes'
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ("id", )

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"
    
    def get_subscription_price(self):
        return self.price*8/10
    
    def display_subscription_price(self):
        return f"{self.get_subscription_price()}"
    
class Reviews(models.Model):
    dish_name = models.CharField(max_length=150, unique=True, verbose_name='Название блюда')
    estimation = models.CharField(max_length=150, unique=True, verbose_name='Оценка')
    comment = models.TextField(verbose_name="Комментарий")

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ("id", )

    def __str__(self):
        return f"{self.dish_name} | {self.estimation}"