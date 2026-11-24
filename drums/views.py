from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .forms import AddParticipantForm, AddPaymentForm, AddStatementForm
from .models import Participant, Payment, Statement


def get_home_page(request):
    statement = Statement.objects.order_by('-pk').first()
    payments = Payment.objects.all()[:10]
    total = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    context = {'statement': statement, 'payments': payments, 'total': total}
    return render(request, 'home.html', context)


def get_parts_page(request):
    participants = Participant.objects.all()
    context = {'participants': participants}
    return render(request, 'parts.html', context)


def get_history_page(request):
    payments = Payment.objects.all()
    total = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    context = {'payments': payments, 'total': total}
    return render(request, 'history.html', context)


def get_account_page(request):
    context = {}
    return render(request, 'account.html', context)


@staff_member_required
def get_add_page(request):
    add_participant = AddParticipantForm()
    add_payment = AddPaymentForm()
    add_statement = AddStatementForm()

    if request.method == 'POST':
        if 'add_participant' in request.POST:
            add_participant = AddParticipantForm(request.POST, request.FILES)
            if add_participant.is_valid():
                participant = Participant(name=add_participant.cleaned_data.get('name'),
                                          photo=add_participant.cleaned_data.get('photo'))
                participant.save()
                messages.success(request, "Участник успешно добавлен.")
                return redirect('add')
        elif 'add_payment' in request.POST:
            add_payment = AddPaymentForm(request.POST)
            if add_payment.is_valid():
                payment = Payment(date=add_payment.cleaned_data.get('date'),
                                  amount=add_payment.cleaned_data.get('amount'),
                                  participant=add_payment.cleaned_data.get('participant'))
                payment.save()
                messages.success(request, "Платеж успешно добавлен.")
                return redirect('add')
        elif 'add_statement' in request.POST:
            add_statement = AddStatementForm(request.POST, request.FILES)
            if add_statement.is_valid():
                statement = Statement(image=add_statement.cleaned_data.get('image'))
                statement.save()
                messages.success(request, "Состояние счета обновлено.")
                return redirect('add')

    context = {'add_participant': add_participant, 'add_payment': add_payment, 'add_statement': add_statement}
    return render(request, 'add.html', context)


@staff_member_required
def get_total_page(request):
    participants = Participant.objects.annotate(total_amount=Sum('payment__amount'))
    context = {'participants': participants}
    return render(request, 'total.html', context)
