from django.shortcuts import render, get_object_or_404
from .models import jobs

def portfolio(request):
	job = jobs.objects
	return render(request, 'portfolio/home.html', {'job':job})
# Create your views here.

def detail(request, job_id):
	job_detail = get_object_or_404(jobs, pk=job_id)
	return render(request, 'portfolio/detail.html', {'job': job_detail})