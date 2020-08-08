from django.shortcuts import render

# Create your views here.
from .models import LessonCPD
from .models import SchoolCPD
import csv

def add_to_db(request):
	with open('C:\\Users\\Indu Reddy\\Desktop\\LessonCPD.csv','rt') as f:
		data=list(csv.reader(f))
		dates=data[0][2:]
		for row in data[1:]:
			for i in range(len(dates)):
				temp_lesson=LessonCPD(tech=row[0],code=row[1],date=dates[i],count=row[2+i])
				temp_lesson.save()


def add_to_db2(request):
	with open('C:\\Users\\Indu Reddy\\Desktop\\SchoolCPD.csv','rt') as f:
		data=list(csv.reader(f))
		dates=data[0][7:]
		for row in data[1:]:
			for i in range(len(dates)):
				temp_lesson=SchoolCPD(reg_date=row[0],city=row[1],school_name=row[2],fee_segment=row[3],board=row[4],total_teachers=row[5],total_students=row[6],date=dates[i],count=row[7+i])
				temp_lesson.save()
