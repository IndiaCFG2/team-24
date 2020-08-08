from django.shortcuts import render
from .models import lesson1,school1
import csv

# Create your views here.
# def add_to_db(request):
#     with open ('C:\\Users\\varun\\Desktop\\321.csv','rt') as f:
#         data=list(csv.reader(f))
#         dates = data[0][2:]
#         for row in data[1:]:
#             for i in range(len(dates)):
#                 temp_lesson=lesson1(tech=row[0], code=row[1], date=dates[i], count=row[2+i])
#                 temp_lesson.save()
#                 #idi try 
def add_to_db(request):
    with open('C:\\Users\\varun\\Desktop\\321-2.csv','rt') as f:
        data=list(csv.reader(f))
        dates=data[0][7:]
        for row in data[1:]:
            for i in range(len(dates)):
                temp_school=school1(city=row[1], school=row[2], fee=row[3],board=row[4],teachers=row[5],students=row[6],date=dates[i],count=row[7+i])
                temp_school.save()
