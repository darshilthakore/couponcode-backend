from django.db import models



COUPON_TYPES = [
    ("FLAT", "FLAT"),
    ("PERCENTAGE", "PERCENTAGE"),
]
# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    coupon_type = models.CharField(max_length=25, choices=COUPON_TYPES)
    discount = models.FloatField(default = 0)
    maximum_discount = models.FloatField(null=True)
    