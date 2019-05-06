from django.shortcuts import render
from .models import *
def shop(request):
    products=product.objects.filter(publication_status=1)
    context={
        "title":"home",
        "content":"home",
        "products":products
    }
    return render(request,"index.html",context)
