from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Quote(models.Model):
	quote = models.TextField(max_length=250)
	speaker = models.CharField(max_length=45)
	FAMILY = 'Fa'
	FRIENDSHIP = 'Fr'
	HAPPINESS = 'Ha'
	HUMOR = 'Hu'	
	LIFE = 'Li'
	SUCCESS ='Su'
	WISDOM = 'Wi'

	
	CATEGORY_CHOICES = (
		(FAMILY, 'Family'),
		(FRIENDSHIP, 'Friendship'),
		(HAPPINESS, 'Happiness'),
		(HUMOR, 'Humor'),
		(LIFE, 'Life'),
		(SUCCESS, 'Success'),
		(WISDOM, 'Wisdom')
	)
	
	category = models.CharField(
		max_length=2,
		choices=CATEGORY_CHOICES,
		blank = False,
		default=LIFE,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)