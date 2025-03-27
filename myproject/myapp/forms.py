from django import forms
from .models import Employee


class BaseEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 10000:
            raise forms.ValidationError('Salary must be greater than 10000')
        return salary


class EmployeeForm(BaseEmployeeForm):
    class Meta(BaseEmployeeForm.Meta):
        pass

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True
