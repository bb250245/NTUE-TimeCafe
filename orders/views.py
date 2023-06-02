from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.generic import TemplateView
from products.models import Product

class CartView(TemplateView):
    template_name = "orders/cart.html"

    def get(self, request, *args, **kwargs):
        product_dict = {}
        product = Product.objects.all().first()
        product_dict[product.id] = {
            "count": 1,
            "product": product
        }
        return self.render_to_response(context)

# Create your views here.
