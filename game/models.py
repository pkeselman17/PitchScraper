from django.db import models
from django.utils import timezone

class Game(models.Model):
	
	sport = models.ForeignKey('Sport')
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	description = models.CharField(max_length=300)
	date = models.DateTimeField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.description
	
	class Meta:
		db_table = 'game'
	