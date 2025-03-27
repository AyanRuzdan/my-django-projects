
# Define Employee Model

```python
class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('Finance', 'Finance'),
        ('Engineering', 'Engineering'),
        ('Marketing', 'Marketing'),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def _str_(self):
        return self.name
```

## Define Employee ModelForm

```python
class BaseEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '_all_'

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 10000:
            raise forms.ValidationError("Salary must be greater than 10,000.")
        return salary

class EmployeeForm(BaseEmployeeForm):
    class Meta(BaseEmployeeForm.Meta):
        pass

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True
```

## Define the View

```python
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
            return HttpResponse('employee_success')  # Redirect to a success page
        
        return render(request, self.template_name, {'form': form})
```
