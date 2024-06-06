from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import CustomerRegistrationForm
from django.contrib import messages

def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        title = products[0].title if products else None
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully.")
            return redirect('home')  # Redirect to home page after successful registration
        else:
            messages.warning(request, "Invalid input data")
        return render(request, 'app/customerregistration.html', locals())

class ProfileView(View):
    def get(self, request):
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        return render(request, 'app/profile.html', locals())
