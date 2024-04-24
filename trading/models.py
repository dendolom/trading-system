from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    buy_order = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def order_value(self):
        return self.quantity * self.stock.price
