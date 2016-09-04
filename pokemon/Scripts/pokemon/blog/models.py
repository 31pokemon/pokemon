from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Type(models.Model):
	type_name=models.CharField(max_length=20)
	definition=models.TextField()
	
	def __str__(self):
		return self.type_name

class Monster(models.Model):
	pokemon_id = models.CharField(max_length=10)
	name = models.CharField(max_length=20)
	type = models.ForeignKey('Type', blank=False, null=False)
	content = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	#編輯過後
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
		
