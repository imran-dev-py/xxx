from django.db import models


class Employee(models.Model):
	eno = models.IntegerField()
	ename = models.CharField(max_length=50)
	esal = models.FloatField()
	eaddr = models.CharField(max_length=50)

	def __str__(self):
		return self.ename 

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'