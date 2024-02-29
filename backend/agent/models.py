from django.db import models
from shortuuidfield import ShortUUIDField 
from vendor.models import Vendor 

class QAGuy(models.Model):
    qa_id = ShortUUIDField(unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    email = models.EmailField()
    pass_code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.vendor} - {self.email}"


class SecurityGuy(models.Model):
    security_id = ShortUUIDField(unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    email = models.EmailField()
    pass_code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.vendor} - {self.email}"