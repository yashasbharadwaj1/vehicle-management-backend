from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField 

class User(AbstractUser):
    user_id = ShortUUIDField(unique=True,max_length=4) 
    email = models.EmailField(unique=True)
    type_of_user = models.CharField(max_length=20, choices=[
        ("customer", "Customer"),
        ("vendor", "Vendor"),
        ("qa_agent", "QA Agent"),
        ("checkout_agent", "Checkout Agent"),
    ], default="customer")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

