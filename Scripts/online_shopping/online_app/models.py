
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'subcategory'

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_img = models.URLField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart_items'

    def __str__(self):
        return f"{self.product.product_name} (x{self.quantity})"

class cloth(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'cloth'




