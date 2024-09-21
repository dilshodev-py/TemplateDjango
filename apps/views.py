from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from apps.forms import EmployeeForm
from apps.models import Employee


# def employee_create_view(request):
#     if request.POST:
#         data = {
#         "first_name" : request.POST.get("first_name"),
#         "last_name" : request.POST.get("last_name"),
#         "email" : request.POST.get("email"),
#         "phone_number" : request.POST.get("phone_number"),
#         "address" : request.POST.get("address"),
#         "password" : request.POST.get("password"),
#         "image" : request.FILES.get("image")
#         }
#         confirm_password = request.POST.get("confirm_password")
#         if data.get('password') != confirm_password:
#             return render(request , 'employee-form.html' , {"error" : "password and confirm not matches"})
#         Employee.objects.create(**data)
#         return redirect('employee-create')
#
#     else :
#         return render(request , 'employee-form.html')


class EmployeeListView(ListView):
    queryset = Employee.objects.all()
    template_name = 'apps/employee-list.html'
    context_object_name = "employees"

class EmployeeFormView(FormView):
    form_class = EmployeeForm
    template_name = 'apps/employee-form.html'
    success_url = reverse_lazy('employee-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_message in form.errors.values():
            messages.error(self.request , error_message[0])
        return super().form_invalid(form)




