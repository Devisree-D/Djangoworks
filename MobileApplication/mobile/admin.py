from django.contrib import admin

# Register your models here.
from mobile.models import Mobile,Brands,Myorders
admin.site.register(Brands)
admin.site.register(Mobile)
admin.site.register(Myorders)