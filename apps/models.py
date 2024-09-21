from django.db.models import CharField, ImageField, EmailField, Model


class Employee(Model):
    first_name  = CharField(max_length=255)
    last_name  = CharField(max_length=255)
    phone_number  = CharField(max_length=13)
    email  = EmailField()
    address  = CharField(max_length=255)
    password  = CharField(max_length=255)
    image  = ImageField(upload_to='employees/%y/%m/%d')



