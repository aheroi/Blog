"""define URL schemes for first_pizzeria"""

from django.urls import path
from .import views

app_name = 'pizzeria_first'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page with list of pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # pizza details page
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]