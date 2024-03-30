from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Token, User, Expense, Income

@csrf_exempt
def submit_expense(request):
    """Submiting expense through POST request"""
    # TODO: validate data - user and amount might be fake or ...

    this_token = request.POST['token']
    user = User.objects.filter(token__token=this_token).get()
    amount = request.POST['amount']
    text = request.POST['text']
    time = datetime.now() if 'date' not in request.POST else request.POST['date']   
    payload = Expense(text=text, date=time, amount=amount, user=user)
    payload.save()
    return JsonResponse({'status': 'OK'})

@csrf_exempt
def submit_income(request):
    """Submiting income through POST request"""
    # TODO: validate data - user and amount might be fake or ...

    this_token = request.POST['token']
    user = User.objects.filter(token__token=this_token).get()
    amount = request.POST['amount']
    text = request.POST['text']
    time = datetime.now() if 'date' not in request.POST else request.POST['date']   
    payload = Income(text=text, date=time, amount=amount, user=user)
    payload.save()
    return JsonResponse({'status': 'OK'})
