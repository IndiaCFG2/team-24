from django.db import models

# Create your models here.
class LessonCPD(models.Model):
	id =models.AutoField(primary_key=True)
	tech=models.CharField(max_length=100)
	code=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	count=models.IntegerField()

class SchoolCPD(models.Model):
	id =models.AutoField(primary_key=True)
	reg_date=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	school_name=models.CharField(max_length=100)
	fee_segment=models.CharField(max_length=100)
	board=models.CharField(max_length=100)
	total_teachers=models.CharField(max_length=100)
	total_students=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	count=models.IntegerField()