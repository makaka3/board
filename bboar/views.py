from django.shortcuts import render
from .models import Product, Rubric
from .forms import ProductForm


def view_index(request):
    products = Product.objects.all()
    rubrics = Rubric.objects.all()

    return render(request, "index.html",
                  context={"products": products, "rubrics": rubrics})


def view_rubric(request, rubric_id):
    products = Product.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)

    return render(request, "rubric.html",
                  context={"products": products,
                           "rubrics": rubrics,
                           "current_rubric": current_rubric})


def view_create_product(request):
    rubrics = Rubric.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.user = request.user
            product.save()
    form = ProductForm()
    return render(request, "create_product.html", context={
        "form": form, "rubrics": rubrics})


def view_product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "product.html", text={"product": product})
