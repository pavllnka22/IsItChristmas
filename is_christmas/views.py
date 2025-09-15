import datetime

from django.shortcuts import render


def is_christmas(request):

    today = datetime.date.today()
    christmas = datetime.date(today.year, 12, 25)

    result = christmas==today

    #return HttpResponse(f"<h1> {'Yes' if result else 'No' }</h1>")
    return render(request, "index.html")