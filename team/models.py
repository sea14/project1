from django.db import models

# Create your models here.

class Member(models.Model):
	image = models.URLField(max_length = 200)
	name = models.CharField(unique = True, max_length = 50)
	position = models.CharField(max_length = 20)
	year = models.CharField(max_length = 10)
	hometown = models.CharField(max_length = 50)
	number = models.CharField(max_length = 2)
	funFact = models.CharField(max_length = 200)

	class Meta(object):
		verbose_name_plural = "Members"
		#ordering = ('name',)

#	def __unicode__(self):
#		return U'%s %s' %(self.name)

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Member, self).save(*args, **kwargs)

class Teams(models.Model):
	image = models.URLField(max_length = 200)
	name = models.CharField(unique = True, max_length = 200)
	coach = models.CharField(max_length = 200)
	wins = models.CharField(max_length = 3)
	losses = models.CharField(max_length = 3)
	members = models.ManyToManyField(Member)

#	class Meta(object):
#		verbose_name_plural = "Teams"

#	def __unicode__(self):
#		return U'% %s' %(self.name)	
