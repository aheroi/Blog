from django.db import models
from matplotlib.pyplot import text, title

# Create your models here.

class BlogPost(models.Model):
    """topic for blog"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blogs'

    def __str__(self) -> str:
        if len(self.title) < 50:
            return f"""{self.title[:50]} {self.text[:250]}"""
        else:
            # return f"\n\t{self.title}\n"
            return f"""{self.title[:50]}... {self.text[:250]}..."""

            