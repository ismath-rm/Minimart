from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    discount = models.FloatField(default=0.0)

    def get_final_price(self):
        return self.product.cost * self.qty * (1 - self.discount / 100)
