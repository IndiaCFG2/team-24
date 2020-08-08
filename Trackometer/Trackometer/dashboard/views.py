from django.shortcuts import render

# Create your views here.

def dash(request):
	return render(request,'dashboard/main/dashboard.html')