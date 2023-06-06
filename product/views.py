from itertools import product
from django.shortcuts import render, get_object_or_404
from product.models import Product
# Create your views here.
def product(request):
 q = request.GET.get('q', None)
 product = ''
 if q is None or q is "":
    product = Product.objects.all()
 elif q is not None:
    product = Product.objects.filter(title__contains=q)

 return render(request, 'Order.html', {'product': product })

def detail(request, id=None):
   product = get_object_or_404(Product, id=id)
   return render(request, 'detail.html', locals())