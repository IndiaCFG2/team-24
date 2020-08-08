from django.db import models

class admins(models.Model):
    school_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    curriculum=models.CharField(max_length=60)

class schools(models.Model):
    school_id = models.ForeignKey(admins,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    grade=models.CharField(max_length=60)
    subject=models.CharField(max_length=70)
    week=models.IntegerField()
    day=models.CharField(max_length=60)
    link=models.CharField(max_length=60)

class lesson1(models.Model):
    id = models.AutoField(primary_key=True)
    tech = models.CharField(max_length=60)
    code = models.CharField(max_length=100)
    date = models.CharField(max_length=60)
    count = models.IntegerField()

class school1(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=60)
    school = models.CharField(max_length=100)
    fee = models.CharField(max_length=100,blank=True)
    board = models.CharField(max_length=100)
    teachers = models.IntegerField()
    students = models.IntegerField()
    date = models.CharField(max_length=60)
    count = models.IntegerField()
