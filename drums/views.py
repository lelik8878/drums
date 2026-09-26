from django.shortcuts import render

def get_home_page(request):
    context = {}
    return render(request, 'home.html', context)
