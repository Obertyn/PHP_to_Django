from django.shortcuts import render
from django.http import HttpResponse


def page1(request):
    return render(request, 'Page1.html')


def page2(request):
    try: countbuns = int(request.POST.get('buns'))
    except:
        countbuns = 0
    try: countdonuts = int(request.POST.get('donuts'))
    except:
        countdonuts = 0
    price = round(countbuns*0.99+countdonuts*1.29, 2)

    context = {
        'price': price,
        'countbuns': countbuns,
        'countdonuts': countdonuts,
    }
    return render(request, 'Page2.html', context)
