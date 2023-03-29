from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

@login_required
def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = order.product.price * order.quantity
            order.save()
            return redirect('store:order_confirmation', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'store/new_order.html', {'form': form})

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'store/order_confirmation.html', {'order': order})
