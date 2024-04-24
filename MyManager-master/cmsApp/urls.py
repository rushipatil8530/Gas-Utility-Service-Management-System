from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cmsApp.views import (
    DashboardPageView,
    CustomersPageView,
    AddCustomerPageView,
    UpdateCustomerPageView,
    DeleteCustomerPageView,
    OrdersPageView,
    AddOrderPageView,
    UpdateOrderPageView,
    DeleteOrderPageView,
    SignupPageView,
    LoginPageView,
    LogoutView
)

urlpatterns = [
    path('', DashboardPageView, name='dashboard_page'),

    path('customers/', CustomersPageView, name="customers_page"),
    path('add_customer', AddCustomerPageView, name="add_customer_page"),
    path('update_customer/<str:customer_id>', UpdateCustomerPageView, name="update_customer_page"),
    path('delete_customer/<str:customer_id>', DeleteCustomerPageView, name="delete_customer_page"),

    path('orders/', OrdersPageView, name="orders_page"),
    path('add_order', AddOrderPageView, name="add_order_page"),
    path('update_order/<str:order_id>', UpdateOrderPageView, name="update_order_page"),
    path('delete_order/<str:order_id>', DeleteOrderPageView, name="delete_order_page"),

    path('signup', SignupPageView, name='signup_page'),
    path('login', LoginPageView, name='login_page'),
    path('logout', LogoutView, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)