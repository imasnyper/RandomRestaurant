from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    dish_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    datetime_ordered = models.DateTimeField(default=timezone.now)
    datetime_fulfilled = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.dish_name}"

    def __repr__(self):
        return f"Order: {self.dish_name}"
