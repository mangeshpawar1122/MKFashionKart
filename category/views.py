from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from store.models import Product

def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(
        Product,
        category__slug=category_slug,
        slug=product_slug,
        is_available=True
    )

    # 🔹 Similar products (same category)
    similar_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(id=product.id)[:6]

    context = {
        'product': product,
        'similar_products': similar_products,
    }

    return render(request, 'store/product_detail.html', context)
