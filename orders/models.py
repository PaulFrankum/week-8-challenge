# from django.conf import settings
from django.db import models
from django.utils import timezone

class orders(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.customer_name
    