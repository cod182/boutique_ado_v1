from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JrPOfDik2SSUzx7pI1JqSpdhVziK59W9cYseieZ4ar40sRKmr9wbOxyfKBHSHZT48kREicjQ033cd79qWcO1Cpi000qqdC2Mu',
    }

    return render(request, template, context)