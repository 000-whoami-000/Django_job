from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=225)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
