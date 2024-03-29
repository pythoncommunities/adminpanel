from django.db import models
from django.utils import timezone
class Pages(models.Model):
	page_title = models.CharField(max_length=250)
	page_slug = models.TextField(default="")
	page_banner = models.TextField(default="")
	page_excerpt = models.TextField(default="")
	page_description = models.TextField(default="")
	page_author = models.IntegerField(default=0)
	page_parent = models.IntegerField(default=0)
	page_order = models.IntegerField(default=0)
	#page_category = models.IntegerField(default=0)
	page_subheading = models.CharField(max_length=250,default="")
	page_status = models.CharField(max_length=250,default="publish")
	page_visible = models.CharField(max_length=250,default="public")
	meta_title = models.CharField(max_length=250,default="")
	meta_keyword = models.CharField(max_length=250,default="")
	meta_description = models.CharField(max_length=250,default="")
	page_access_level = models.CharField(max_length=250,default="[]")
	page_created= models.DateTimeField('created',default=timezone.now)
	page_updated= models.DateTimeField('created',default=timezone.now)
