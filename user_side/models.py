from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    cost = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    payment_type = models.PositiveSmallIntegerField(default=1)
    region = models.CharField(null=True, blank=False, max_length=100)
    city = models.CharField(null=True, blank=False, max_length=100)
    address = models.CharField(null=False, blank=False, max_length=250)
    status = models.PositiveSmallIntegerField(default=1, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('status', '-created_at')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    amount = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("-created_at",)
