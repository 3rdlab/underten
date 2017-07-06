from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	brand = models.ForeignKey('BrandList')
	description = models.TextField()
	
	#price = models.DecimalField(max_digits=8, deciaml_places=2)
	price = models.PositiveSmallIntegerField(default=0)
	original_url = models.CharField(max_length=200)
	image_url1 = models.CharField(max_length=200)
	#image_url2 = models.TextField(validators=[URLValidator()])

	#for_whom = men, women, kids, baby
	#categoy = top, shoes, pants, neat

	def __unicode__(self):              # __unicode__ on Python 2
		return self.name



class BrandList(models.Model):
	brand_name = models.CharField(max_length=50)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.brand_name



# User review of Products
class Review(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published', auto_now=True)
	modified_date = models.DateTimeField(null=True)
	
	ups = models.PositiveSmallIntegerField(default=0)
	downs = models.PositiveSmallIntegerField(default=0)
	views = models.PositiveSmallIntegerField(default=0)

	product = models.ManyToManyField(Product, null=True, blank=True)
	

	#category_id = models.ForeignKey('ArticleCategory')
	#author_id = models.IntegerField()

	def __unicode__(self):
		#return self.title
		return self.title


	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'