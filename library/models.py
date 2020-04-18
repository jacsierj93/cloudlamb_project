from django.db import models

# Create your models here.

class Writer(models.Model):
	name = models.CharField(max_length = 200, unique=True)
	bio = models.CharField(max_length = 1000)

	def 	__str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length = 200)
	resume = models.CharField(max_length = 500)
	year = models.IntegerField(default = 2020)
	writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


# TODO: Modelo para Usuario
	#Nombre
	#Email
	#Fecha_nacimiento
	#password
	#fecha_registro

#TODO: Modelo Genero.
	#Nombre
	#Descripcion
