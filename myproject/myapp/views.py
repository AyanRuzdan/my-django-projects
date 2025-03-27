from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse

class EmployeeView(View):
    template_name = 'employee_form.html'

    def get(self, request, employee_id=None):
        if employee_id:
            employee = get_object_or_404(Employee, id=employee_id)
            form = EmployeeForm(instance=employee)
        else:
            form = EmployeeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, employee_id=None):
        if employee_id:
            employee = get_object_or_404(Employee, id=employee_id)
            form = EmployeeForm(request.POST, request.FILES, instance=employee)
        else:
            form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('employee success')

        return render(request, self.template_name, {'form': form})
