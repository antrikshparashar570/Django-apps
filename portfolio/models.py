from django.db import models

class jobs(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
# Create your models here.

	def __str__(self):
		return self.summary