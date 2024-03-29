from django.db import models
from userauths.models import User
from shortuuidfield import ShortUUIDField
from backend.storage_backends import PublicMediaStorage


class Vendor(models.Model):
    vendor_id = ShortUUIDField(unique=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200, default="details", blank=True)

    def __str__(self):
        return self.name



class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(default="KAO4KD8347", max_length=10)
    product_id = ShortUUIDField(unique=True)
    product_image = models.FileField(
        storage=PublicMediaStorage(), upload_to="product", default="default.jpg"
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
    order_id = ShortUUIDField(unique=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_booking = models.DateTimeField(auto_now_add=True)
    # date chosen by the security agent, when user comes to vendors place to collect his/her vehicle
    delivery_date = models.DateTimeField(null=True, blank=True)
    # purchase_order_number = order_id(underscore)date_of_booking
    purchase_order_number = models.CharField(max_length=255, unique=True)
    # delivery_challan_number = order_id(underscore)delivery_date
    delivery_challan_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.date_of_booking}"

    class Meta:
        ordering = ["-date_of_booking"]
