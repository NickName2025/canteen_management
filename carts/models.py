from django.db import models
from student.models import Dishes

from users.models import User


class CartQueryset(models.QuerySet):

    def test(self):
        return "123"
    
    def total_price(self):
        return sum(cart.dishes_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    dish = models.ForeignKey(to=Dishes, on_delete=models.CASCADE, verbose_name='Блюда')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    final_prices = models.TextField(verbose_name='Итоговые цены')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    objects = CartQueryset().as_manager()

    def dishes_price(self):
        s = [float(i) for i in self.final_prices.split("|")[:-1]]
        return round(sum(s), 2)

    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.dish.name} | Количество {self.quantity}'