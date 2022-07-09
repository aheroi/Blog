from pyexpat import model
from django.db import models
from matplotlib.pyplot import cla, text
# Create your models here.

class Pizza(models.Model):
    """types of pizza"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """return str presentation name of pizza"""
        return self.text


class Entry(models.Model):
    """class for toppings"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self) -> str:
        """return str presentation of toppings"""
        if len(self.text) < 50:
            return f'{self.text[:50]}'
        else:
            return f'{self.text[:50]}...'
