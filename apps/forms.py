from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ()
        # fields = "",

    def clean_phone_number(self):
        phone_number = self.clean().get("phone_number")
        if not phone_number.isdigit() or len(phone_number) != 12:
            raise ValidationError("phone number invalid")
        return phone_number

    def clean_password(self):
        password = self.clean().get("password")
        if len(password) < 4:
            raise ValidationError("password invalid")
        return password




