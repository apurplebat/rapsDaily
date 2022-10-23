from django.conf import settings
from django.db import models

# Create your models here.


class Topic(models.Model):
	RAPTORS = 'Raptors'

	name = models.CharField(
		max_length=50,
		unique=50,
		null=False,
		default=RAPTORS,
		help_text='Name for topic',
	)


	slug = models.SlugField(
		null=False,
		help_text='Slug for the topic',
		unique=True,  # Slug is unique for topic name
    )

	class Meta:
		# Sort by the `created` field. The `-` prefix
		# specifies to order in descending/reverse order.
		# Otherwise, it will be in ascending order.
		ordering = ['name']


	def __str__(self):
		return self.name





class Post(models.Model):
	DRAFT = 'draft'
	PUBLISHED = 'published'
	STATUS_CHOICES = [
		(DRAFT, 'Draft'),
		(PUBLISHED, 'Published')
	]


	title = models.CharField(max_length=255)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)  # Sets on create
	updated = models.DateTimeField(auto_now=True)  # Updates on each save
	status = models.CharField(
		max_length=10,
		choices=STATUS_CHOICES,
		default=DRAFT,
		help_text='Set to "published" to make this post publicly visible',
	)
	published = models.DateTimeField(
		null=True,
		blank=True,
		help_text='The date & time this article was published',
	)
	slug = models.SlugField(
		null=False,
		help_text='The date & time this article was published',
		unique_for_date='published',  # Slug is unique for publication date
    )


	class Meta:
		# Sort by the `created` field. The `-` prefix
		# specifies to order in descending/reverse order.
		# Otherwise, it will be in ascending order.
		ordering = ['-created']

	author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',  # "This" on the user model
        null=False
    )

	topics = models.ManyToManyField(
        Topic,  # associating topics with posts
        related_name='blog_posts'  # related name
    )


	def __str__(self):
		return self.title






class Comment(models.Model):

	post = models.ForeignKey(
        Post,  # associating posts with comments
        on_delete=models.CASCADE,
        related_name='comments',  # related name
        null=False
    )
	name = models.CharField(
		max_length=40,
		null=False
	)
	email = models.EmailField(null=False)
	text = models.TextField(
		max_length=150,
		null=False
	)
	approved = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)  # Sets on create
	updated = models.DateTimeField(auto_now=True)  # Updates on each save


	class Meta:
		# Sort by the `created` field. The `-` prefix
		# specifies to order in descending/reverse order.
		# Otherwise, it will be in ascending order.
		ordering = ['-created']


	def __str__(self):
		return '{} replied "{}"'.format(self.name, self.text)