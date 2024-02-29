from django.contrib import admin
from .models import User 

admin.site.register(User)

admin.site.site_title = "Vehicle management system Administration"
admin.site.site_header = "Vehicle management system"
admin.site.index_title = "Administration"
