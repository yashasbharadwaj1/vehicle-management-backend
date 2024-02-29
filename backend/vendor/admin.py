from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(QAGuy)
admin.site.register(SecurityGuy)
admin.site.register(Order)

