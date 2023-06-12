from django.shortcuts import render
from .forms import DataQueryForm

def resume(request):
    return render(request, 'database/resume.html')

def dataquery(request):
    dq_form = DataQueryForm()

    context = {
        "dq_form": dq_form
    }
    return render(request, "database/request_data.html", context)
