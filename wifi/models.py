from django.db import models

import datetime


class Customer(models.Model):
    name = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date published')
    expaire_date = models.DateTimeField(null=True)
    id_card = models.FileField(upload_to='uploads/')
    phone = models.CharField(max_length=30)
    address = models.TextField()
    wifi_plan = models.IntegerField()
    monthly_bill = models.FloatField()
    payment_method = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    agent_name = models.CharField(max_length=100,null=True)
    bill_address = models.TextField(null=True)
    router_id = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return self.name


class UserMain(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name


class Payments(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staf_id = models.ForeignKey(UserMain, on_delete=models.CASCADE)
    pay_date = models.DateField(default=datetime.date.today)
    pay_amount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    due = models.FloatField()
    note = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.cust_id)



        # name = models.ForeignKey(Customer, on_delete=models.CASCADE)
