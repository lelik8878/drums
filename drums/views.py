from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddParticipantForm, AddPaymentForm, AddStatementForm
from .models import Participant, Payment, Statement


def get_home_page(request):
    statement = Statement.objects.order_by('-pk').first()
    print(statement)
    print(type(statement))
    context = {'statement': statement}
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


def get_add_page(request):
    add_participant = AddParticipantForm()
    add_payment = AddPaymentForm()
    add_statement = AddStatementForm()

    if request.method == 'POST':
        if 'name' in request.POST:
            add_participant = AddParticipantForm(request.POST, request.FILES)
            if add_participant.is_valid():
                participant = Participant(name=add_participant.cleaned_data.get('name'),
                                          photo=add_participant.cleaned_data.get('photo'))
                participant.save()
                messages.success(request, "Участник успешно добавлен.")
                return redirect('add')
        elif 'amount' in request.POST:
            add_payment = AddPaymentForm(request.POST)
            if add_payment.is_valid():
                payment = Payment(date=add_payment.cleaned_data.get('date'),
                                  amount=add_payment.cleaned_data.get('amount'),
                                  participant=add_payment.cleaned_data.get('participant'))
                payment.save()
                messages.success(request, "Платеж успешно добавлен.")
                return redirect('add')
        elif 'image' in request.FILES:
            add_statement = AddStatementForm(request.POST, request.FILES)
            if add_statement.is_valid():
                statement = Statement(image=add_statement.cleaned_data.get('image'))
                statement.save()
                messages.success(request, "Состояние счета обновлено.")
                return redirect('add')

    context = {'add_participant': add_participant, 'add_payment': add_payment, 'add_statement': add_statement}
    return render(request, 'add.html', context)


def get_total_page(request):
    context = {}
    return render(request, 'total.html', context)
