from django.shortcuts import render

def resume(request):
    return render(request, 'database/resume.html')
