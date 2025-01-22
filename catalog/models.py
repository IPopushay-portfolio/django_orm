from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.CharField(verbose_name='Категория', unique=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']


    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return {self.name}





class Category(models.Model):
    prod_cat = models.CharField(max_length=150, verbose_name='Наименование', unique=True)
    description_cat = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['prod_cat']


    def __str__(self):
        return self.prod_cat
