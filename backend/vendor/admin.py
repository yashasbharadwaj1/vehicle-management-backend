from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(OrderLifeCycle)
