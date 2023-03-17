from django.forms import ModelForm
from django.shortcuts import redirect, render
from projects.models import Product, Cart

# Create your views here.

def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    print(product.image)
    return render(request, 'product_detail.html', context)

def cart(request):
    cart = Cart.objects.all()
    total = 0;
    for item in cart:
        total += item.product.price * item.qty
    context = {
        'cart': cart,
        'total': total
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, pk):
    try:
        item = Cart.objects.get(pk=pk)
    except:
        item = Cart(id=pk)
        item.qty = 0;
        item.product = Product.objects.get(pk=pk)
    finally:
        if request.method == 'POST':
            item.qty += 1
            item.save()
    return redirect('cart')


def save_cart(request):
    print(request.POST.getlist('qty'))
    print(request.POST.getlist('product_pk'))
    pklist = request.POST.getlist('product_pk')
    qtylist = request.POST.getlist('qty')
    for i in range(len(pklist)):
        pk = pklist[i]
        qty = int(qtylist[i])
        item = Cart.objects.get(pk=pk)
        print(" ** ")
        item.qty = qty
        item.save()
    return redirect('cart')

    
def cart_delete(request, pk):
    product = Cart.objects.get(pk=pk)
    print(product)
    product.delete()
    return redirect('cart')