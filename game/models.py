from django.db import models

class Game(models.Model):
	
	sport = models.ForeignKey('Sport')
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	description = models.CharField(max_length=300)
	
	def __str__(self):
		return self.description
	
	class Meta:
		db_table = 'game'
	