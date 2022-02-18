from django.db import models


class Product(models.Model):
    saree_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added')
    in_stock = models.BooleanField()
    image_path = models.CharField(max_length=200)

    def __str__(self):
        return self.saree_name


class Account(models.Model):
    account_number = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=200)
    account_holder_name = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    is_active = models.BooleanField()

    def __str__(self):
        return self.bank_name + self.account_number[-5:]


class UPI(models.Model):
    upi_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()

    def __str__(self):
        return self.upi_id