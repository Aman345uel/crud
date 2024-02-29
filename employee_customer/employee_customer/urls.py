
from django.contrib import admin
from django.urls import path
from emp_cust.views import employee_list, employee_create,employee_update,employee_delete,customer_list,customer_create,customer_update,customer_delete


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', employee_list, name='employee_list'),
    path('employees/create/', employee_create, name='employee_create'),
    path('employees/<int:pk>/update/',employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', employee_delete, name='employee_delete'),

    path('customers/', customer_list, name='customer_list'),
    path('customers/create/', customer_create, name='customer_create'),
    path('customers/<int:pk>/update/', customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', customer_delete, name='customer_delete'),
]
