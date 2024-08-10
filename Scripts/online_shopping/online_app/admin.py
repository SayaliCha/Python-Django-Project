from django.contrib import admin
from .models import *
from .models import Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['subcategory_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['category','subcategory','product_name','product_img','price','description']



