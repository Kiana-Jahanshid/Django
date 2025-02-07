from django.shortcuts import render 


def index(request):
    return render(request , template_name="index.html")


def products(request ):
    return render(request , template_name="products.html")
