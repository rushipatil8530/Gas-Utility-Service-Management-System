from django.contrib import admin

from cmsApp.models import (
    Customer,
    Order,
)



# Model created for Customer for Admin Panel
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "date_created"]


# Model created for Order for Admin Panel
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'customer', 'date_created')


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)

