from django.db import models

class Sport(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	
	class Meta:
		db_table = 'sport'