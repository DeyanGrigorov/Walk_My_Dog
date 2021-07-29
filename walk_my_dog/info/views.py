from django.shortcuts import render


def how_it_works(request):
    return render(request, 'info/how_it_works.html')
