from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Search


def index(request):
    """main page"""
    return render(request, "index.html", {'message': 'Please, enter your number to check'})


def contacts(request):
    """contacts page"""
    return render(request, "contacts.html", {})


def about(request):
    """contacts page"""
    return render(request, "about.html", {})


def get_number(request):
    if request.method == 'POST':
        number_to_check = int(request.POST.get('number_to_check'))
        c = int(0)
        while number_to_check != 1 and c != 10000 or 10000 > c:
            b = int(0)
            while number_to_check % 10 != 0 or number_to_check > 9:
                b = b + ((number_to_check % 10) * (number_to_check % 10))
                number_to_check = int(number_to_check / 10)
            b = b + number_to_check * number_to_check
            c = c + 1
            number_to_check = b
        if number_to_check == 1:
            return render(request, "detail.html", {'message': 'Your number is HAPPY! '})
        else:
            return render(request, "detail.html", {'message': 'Your number is SAD '})

