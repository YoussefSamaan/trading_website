from django import http
from django.shortcuts import render


def front_page(request):
    return render(request, 'stocks/frontpage.html')
