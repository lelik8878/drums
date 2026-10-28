from django.shortcuts import render


def get_home_page(request):
    context = {}
    return render(request, 'home.html', context)


def get_parts_page(request):
    context = {}
    return render(request, 'parts.html', context)


def get_history_page(request):
    context = {}
    return render(request, 'history.html', context)


def get_account_page(request):
    context = {}
    return render(request, 'account.html', context)
