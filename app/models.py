from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

CATEGORY_CHOICES = (
    ('CR', 'CURD'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),  # Corrected spelling
    ('IC', 'Ice-Creams'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(blank=True)
    prodapp = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product', verbose_name='Product Image')

    def __str__(self):
        return self.title

    def clean(self):
        if self.discounted_price > self.selling_price:
            raise ValidationError(_('Discounted price cannot be greater than the selling price.'))

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
