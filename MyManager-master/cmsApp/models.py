from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=235, null=True)
    email = models.EmailField(max_length=235, null=True)
    phone = models.CharField(max_length=235, null=True)
    address = models.CharField(max_length=235, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "1. Total Customers"

    def __str__(self):
        return self.name

class Order(models.Model):
    status_choices = (
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        ("Out for Delivery", "Out for Delivery"),
    )

    SERVICE_REQUEST_CHOICES = [
        ('gas_cylinder', 'Gas Cylinder'),
        ('other_equipment', 'Other Equipment'),
    ]
    
    customer = models.CharField(max_length=255)  # Allow manual input for customer
    product = models.CharField(max_length=255)   # Allow manual input for product
    status = models.CharField(max_length=235, choices=status_choices)
    date_created = models.DateTimeField(auto_now_add=True)
    service_request_type = models.CharField(max_length=100, choices=SERVICE_REQUEST_CHOICES)
    service_request_attachment = models.FileField(upload_to='static/images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "2. Total Orders"

    def __str__(self):
        return f"Order of {self.customer} | Status - {self.status}"
