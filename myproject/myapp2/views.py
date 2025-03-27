from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse


class ProductView(View):
    template_name = 'product_form.html'

    def get(self, request, product_id=None):
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            form = ProductForm(instance=product)
        else:
            form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, product_id=None):
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            form = ProductForm(request.POST, request.FILES, instance=product)
        else:
            form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('product success') 

        return render(request, self.template_name, {'form': form})
