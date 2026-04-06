from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        if email:
            _, created = Subscriber.objects.get_or_create(email=email, defaults={'name': name})
            if created:
                messages.success(request, "You're subscribed to our newsletter!")
            else:
                messages.info(request, 'This email is already subscribed.')
        return redirect('home')
    return redirect('home')
