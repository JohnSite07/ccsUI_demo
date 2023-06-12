from django.shortcuts import render
from .forms import DataQueryForm
from .variables import *

def resume(request):
    return render(request, 'database/resume.html')

def dataquery(request):
    import psycopg2 as psyco

    conn = psyco.connect(
        host = host,
        database = database,
        user = user,
        password = password
    )

    if request.method == 'POST':
        dq_form = DataQueryForm(request.POST)
        if dq_form.is_valid():
            tableau = dq_form.cleaned_data['tableau']
            table = select(tableau, conn).to_html(index=False,
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
    conn.close

    return render(request, "database/request_data.html", context)
