from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=250, blank=True)
    cat_img = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'      # jevha admin page varti model chya navapudhe 's' lagto tar te na lavta apan swataha lihilel naav admin page par show vhav mhanun 'verbose_name_plural' ha code lihava.

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.name