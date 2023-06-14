from django.shortcuts import render
from .forms import DataQueryForm
from .variables import *
import pandas as pd

def resume(request):
    return render(request, 'database/resume.html')

def dataquery(request):

#    data = exemple_personnels.objects.all()
#    df = pd.DataFrame(list(data.values()))

    if request.method == 'POST':
        dq_form = DataQueryForm(request.POST)
        if dq_form.is_valid():
            tableau = dq_form.cleaned_data['tableau']
            data = data_dic[tableau].objects.all()
            df = pd.DataFrame(list(data.values()))
            table =  df.to_html(index=False,
                                classes=[
                                    "table table-secondary table-hover",
                                    ]
                                  )
            return render(request, "database/data_requested.html", {"table":table})
    else:
        dq_form = DataQueryForm()

    context = {
        "dq_form": dq_form
    }

    return render(request, "database/request_data.html", context)
