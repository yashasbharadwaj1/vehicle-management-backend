from django.db import models
from userauths.models import User
from backend.storage_backends import PublicMediaStorage


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200, default="details", blank=True)

    def __str__(self):
        return self.name



class Vehicle(models.Model):
    TWO_WHEELER = '2W'
    FOUR_WHEELER = '4W'
    THREE_WHEELER = '3W'
    VEHICLE_TYPE_CHOICES = [
        (TWO_WHEELER, '2-wheeler'),
        (FOUR_WHEELER, '4-wheeler'),
        (THREE_WHEELER, '3-wheeler'),
    ]

    type = models.CharField(
        max_length=2,
        choices=VEHICLE_TYPE_CHOICES,
        default=TWO_WHEELER,
    )
    name = models.CharField(max_length=100)
    number = models.CharField(default="KAO4KD8347", max_length=10)
    stock = models.IntegerField(default=0)
    product_image = models.FileField(
        storage=PublicMediaStorage(), upload_to="product", default="product/default.jpg"
    )
    price = models.FloatField()
    qa_assured = models.BooleanField(default=False)
    security_assured = models.BooleanField(default=False)
    qa_rejection_reason = models.CharField(
        max_length=400, default="reason for qa guy to reject"
    )
    security_rejection_reason = models.CharField(
        max_length=400, default="reason for security guy to reject"
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_booking = models.DateField()
    delivery_date = models.DateField()
    # purchase_order_number = order_id(underscore)date_of_booking
    purchase_order_number = models.CharField(max_length=255, unique=True)
    # delivery_challan_number = order_id(underscore)delivery_date
    delivery_challan_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.user_id} - {self.product_id} - {self.date_of_booking}"

    class Meta:
        ordering = ["-date_of_booking"]
