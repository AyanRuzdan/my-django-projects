from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name='employee_form'),
    path('employee/<int:employee_id>/', EmployeeView.as_view(), name='edit_employee'),
]
