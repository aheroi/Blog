from django.shortcuts import render
from .models import Pizza


# Create your views here.

def index(request):
    """home page app Pizzeria"""
    return render(request, 'pizzeria_first/index.html')

def pizzas(request):
    """display the list of pizzas"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria_first/pizzas.html', context)
    
def pizza(request, pizza_id):
    """display one topping and its entries"""
    pizza = Pizza.objects.get(id=pizza_id)                      # database access
    # entries = pizza.entry_set.ordered_by('-date_added')
    entries = pizza.entry_set.order_by('-date_added')   
    context = {'pizza': pizza, 'entries': entries}
    return render(request, 'pizzeria_first/pizza.html', context)
