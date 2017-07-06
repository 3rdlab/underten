from django.contrib import admin
from article.models import Article

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

#class ArticleAdmin(admin.ModelAdmin):
class ArticleAdmin(SummernoteModelAdmin):
	#fields = ['title', 'body', 'pub_date']
	fields = ['title', 'body', 'category']


admin.site.register(Article, ArticleAdmin)
