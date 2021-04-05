from django.shortcuts import render

# Create your views here


def job_page(request):
    context = {
        'page': 1
    }
    return render(request, 'job_position.html', context)


def echarts(request):
    context = {
        'page': 2
    }
    return render(request, 'analysis.html', context)
