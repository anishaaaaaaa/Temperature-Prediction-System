from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.




class Category(models.Model):
	name = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250,unique  = True)



	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('comment_app:list_of_post_by_category',args = [self.slug])



	def __str__(self):
		return self.name


class Post(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('published','Published'),
	)
	category = models.ForeignKey('Category',on_delete = models.CASCADE,) 
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250,unique = True)
	content = models.TextField()
	seo_title = models.CharField(max_length = 250)
	seo_description = models.CharField(max_length = 250)
	author = models.ForeignKey(User,on_delete= models.PROTECT,related_name = 'blog_posts')
	published = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=9,choices = STATUS_CHOICES,default = 'draft')



	def get_absolute_url(self):
		return reverse('comment_app:post_detail',args = [self.slug])


	def __str__(self):
		return self.title

#---------------------------------------------------------------------------------------comment wala part

class Comment(models.Model):
	post = models.ForeignKey('Post', related_name = 'comments',on_delete = models.CASCADE,)
	user = models.CharField(max_length = 250)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	approved = models.BooleanField(default = False)



	def approved(self):
		self.approved = True
		self.save()


	def __str__(self):
		return self.user