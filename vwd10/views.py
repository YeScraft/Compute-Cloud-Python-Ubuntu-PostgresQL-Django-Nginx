from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return redirect('cars_list_url')
