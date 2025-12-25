from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        indexes = [
            models.Index(fields=['title']),
        ]
