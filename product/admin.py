from django.contrib import admin
from product.models import *

from django_summernote.admin import SummernoteModelAdmin

class ProductAdmin(SummernoteModelAdmin):

	#fields = ['title', 'body', 'pub_date']
	fields = ['name', 'brand', 'description', 'price', 'original_url', 'image_url1']

admin.site.register(Product, ProductAdmin)
admin.site.register(BrandList)
admin.site.register(Review)