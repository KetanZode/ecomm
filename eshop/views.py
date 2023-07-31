from django.shortcuts import render
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.http import JsonResponse
# Create your views here.

def prod_list(request):
    pro = Product.objects.all()
    serialized = ProductSerializer(pro, many=True)
    return JsonResponse(serialized.data, safe=False)


def cat_list(request):
    cat = Category.objects.all()
    serialized = CategorySerializer(cat, many=True)
    return JsonResponse(serialized.data, safe=False)

def get_prod(request,slug):
    pro = Product.objects.filter(pslug=slug).first()
    serialized = ProductSerializer(pro)
    return JsonResponse(serialized.data)

def get_prodd(request,pk):
    pro = Product.objects.get(pk=pk)
    serialized = ProductSerializer(pro)
    return JsonResponse(serialized.data)

def getProdCat(request, slug):
    cat = Category.objects.filter(cname=slug).first()
    pro = Product.objects.filter(pcat = cat.id)
    serialized = ProductSerializer(pro, many=True)
    return JsonResponse(serialized.data, safe=False)
