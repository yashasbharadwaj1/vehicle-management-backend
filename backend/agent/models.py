from django.db import models
from vendor.models import Vendor 

class QAGuy(models.Model):
    name = models.CharField(max_length=100,default='name')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    email = models.EmailField()
    pass_code = models.CharField(max_length=8,unique=True)
    def __str__(self):
        return f"{self.vendor} - {self.email}"

class QACheckIn(models.Model):
    qa_guy = models.ForeignKey(QAGuy,on_delete=models.CASCADE)
    unique_checkin_id = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.unique_checkin_id}"
    
class SecurityGuy(models.Model):
    name = models.CharField(max_length=100,default='name')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    email = models.EmailField()
    pass_code = models.CharField(max_length=8,unique=True)

    def __str__(self):
        return f"{self.vendor} - {self.email}" 

class SecurityCheckin(models.Model):
    security_guy = models.ForeignKey(SecurityGuy,on_delete=models.CASCADE)
    unique_checkout_id = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.unique_checkout_id}"
    
