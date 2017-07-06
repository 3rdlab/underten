import datetime

from django.db import models
from django.forms import ModelForm

from mptt.models import MPTTModel, TreeForeignKey

from django.utils import timezone


# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published', auto_now=True)
	likes = models.IntegerField(default = 0)
	category = models.ForeignKey('ArticleCategory', null=True)
	docfile = models.FileField(upload_to='media/%Y/%m/%d', null=True)


	#author_id = models.IntegerField()


	def __unicode__(self):
		return self.title


	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'



class ArticleCategory(MPTTModel):
    name = models.CharField(max_length=60)
    slug = models.CharField(max_length=20, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):              # __unicode__ on Python 2
		return self.name




