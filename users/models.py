from django.db import models

# Create your models here.
class UserType(models.IntegerChoices):
    Admin = 1
    Customer = 2
    Driver = 3

class RegisterUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=12, default='', null=False)
    username = models.CharField(max_length=10, default='', null=False)
    password = models.CharField(max_length=10, default='', null=False)
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.Customer)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
