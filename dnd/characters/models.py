from django.db import models
from django.contrib import admin

# Create your models here.
class Attributes(models.Model):
	"""Represents the attributes a Character has"""
	strength = models.PositiveIntegerField()
	dexterity = models.PositiveIntegerField()
	constitution = models.PositiveIntegerField()
	intelligence = models.PositiveIntegerField()
	wisdom = models.PositiveIntegerField()
	charisma = models.PositiveIntegerField()

class Power(models.Model):
	"""Represents a Power or ability that can be cast."""
	name = models.CharField(max_length=100)
	cast_time = models.PositiveIntegerField()
	recovery_time = models.PositiveIntegerField()
	spell_range = models.PositiveIntegerField()
	potency = models.PositiveIntegerField()
	resolve = models.PositiveIntegerField()
	stamina = models.PositiveIntegerField()
	target = models.CharField(max_length=100)
	duration_segments = models.PositiveIntegerField()
	components = models.CharField(max_length=50)
	effect = models.TextField()
	special = models.TextField()

class Character(models.Model):
	"""Represents a Character a player controls."""
	name = models.CharField(max_length=100, unique=True)
	level = models.PositiveIntegerField()
	race = models.CharField(max_length=50)
	char_class = models.CharField(max_length=50)
	xp = models.PositiveIntegerField()
	sex = models.CharField(max_length=1)
	age = models.PositiveIntegerField()
	weight = models.PositiveIntegerField()
	height = models.PositiveIntegerField()
	size = models.CharField(max_length=1)
	attributes = models.OneToOneField(Attributes)
	powers = models.ManyToManyField(Power)


admin.site.register(Character)
admin.site.register(Power)
admin.site.register(Attributes)