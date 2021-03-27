from django.shortcuts import render

# Create your views here.


def job_page(request):
    return render(request, 'job_position.html')
