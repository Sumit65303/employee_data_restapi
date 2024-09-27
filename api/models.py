from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    company_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),
                                                     ('NON IT','NON IT'),
                                                     ('Mobile','MOBILE'),
                                                     ))
    added_date = models.DateField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    position = models.CharField(max_length=100, choices=(('IT Professional','IT'),
                                                     ('HR Recuriter','NON IT'),
                                                     ('Team Leader','TL'),
                                                     ))
    active = models.BooleanField(default=True)
    Company = models.ForeignKey("Company", on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name