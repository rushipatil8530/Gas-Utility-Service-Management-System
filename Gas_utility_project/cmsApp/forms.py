from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cmsApp.models import Customer, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "John Doe"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "johndoe@gmail.com"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tel +9114000032"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "NH-10, Jhansi, India"}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'address': 'Address',
        }

class OrderForm(forms.ModelForm):
    SERVICE_REQUEST_CHOICES = [
        ('gas_cylinder', 'Gas Cylinder'),
        ('other_equipment', 'Other Equipment'),
    ]
    
    customer = forms.CharField(max_length=255, label='Customer')  # Change to CharField for manual input
    product = forms.CharField(max_length=255, label='Product')    # Change to CharField for manual input
    service_request_type = forms.ChoiceField(choices=SERVICE_REQUEST_CHOICES, label='Service Request Type')
    service_request_attachment = forms.FileField(label='Service Request Attachment', required=False)

    class Meta:
        model = Order
        fields = ['customer', 'product', 'status', 'service_request_type', 'service_request_attachment']
        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'status': 'Status',
        }
class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "John",
        }),
        label="First name"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "Doe",
        }),
        label="Last name"
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "johndoe",
        }),
        label="Username"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "type": "email",
            "placeholder": "johndoe@gmail.com",
        }),
        label="Email"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "type": "password",
        }),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "type": "password",
        }),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
