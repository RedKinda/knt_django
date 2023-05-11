from django.shortcuts import render

# Create your views here.

from django.http import Http404, HttpResponse

from knt_backend.models import Product


def index(request):
    return HttpResponse("Hello, world. You're at the knt index.")


def product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return HttpResponse(
        "You're looking at product %s. name: %s, price: %s "
        % (product_id, product.name, product.price)
    )
