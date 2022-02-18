from django.shortcuts import render
from .models import Product, Account, UPI

def index(request):
    saree_list = Product.objects.filter(in_stock=True)
    context = {'saree_list': saree_list}
    return render(request, 'landingPage/index.html', context)

def payment(request):
    accounts_list = Account.objects.filter(is_active=True)
    upi_list = UPI.objects.filter(is_active=True)
    context = {'accounts_list': accounts_list, 'upi_list': upi_list}
    return render(request, 'landingPage/payment.html', context)