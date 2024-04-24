from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cmsApp.models import Customer, Order
from cmsApp.forms import CustomerForm, OrderForm, SignupForm


def DashboardPageView(request):
    total_orders = Order.objects.all().count()
    orders_pending = Order.objects.filter(status="Pending").count()
    orders_delivered = Order.objects.filter(status="Delivered").count()
    orders_out_for_delivery = Order.objects.filter(status="Out for Delivery").count()

    context = {
        "total_orders": total_orders,
        "orders_pending": orders_pending,
        "orders_delivered": orders_delivered,
        "orders_out_for_delivery": orders_out_for_delivery,
    }
    return render(request, 'dashboard_page.html', context)


@login_required(login_url="login_page")
def CustomersPageView(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers,
    }
    return render(request, 'customers_page.html', context)


@login_required(login_url="login_page")
def AddCustomerPageView(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully.")
            return redirect('add_customer_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


@login_required(login_url="login_page")
def UpdateCustomerPageView(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully.")
            return redirect('customers_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


@login_required(login_url="login_page")
def DeleteCustomerPageView(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    messages.error(request, "Customer deleted successfully.")
    return redirect('customers_page')


@login_required(login_url="login_page")
def OrdersPageView(request):
    orders = Order.objects.all()
    context = {
        "orders": orders,
    }
    return render(request, 'orders_page.html', context)


def AddOrderPageView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order added successfully.")
            return redirect('add_order_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


@login_required(login_url="login_page")
def UpdateOrderPageView(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order updated successfully.")
            return redirect('orders_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


@login_required(login_url="login_page")
def DeleteOrderPageView(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    messages.error(request, "Order deleted successfully.")
    return redirect('orders_page')


def SignupPageView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Account created successfully.")
                return redirect('signup_page')
            else:
                messages.error(request, "Some error occurred!")
                return redirect('signup_page')
        else:
            signup_form = SignupForm()
        context = {'signup_form': signup_form}
        return render(request, 'registration/signup_page.html', context)
    else:
        return redirect('/')


def LoginPageView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully.")
                return redirect('dashboard_page')
            else:
                messages.error(request, "Invalid credentials!")
                return redirect('login_page')
        return render(request, 'registration/login_page.html')
    else:
        return redirect("/")


@login_required(login_url="login_page")
def LogoutView(request):
    logout(request)
    return redirect('login_page')
