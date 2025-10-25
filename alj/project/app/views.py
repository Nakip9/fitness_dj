from django.shortcuts import render, redirect
from .models import Session
from .forms import RegisterForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404


def home(request):
    sessions = Session.objects.all()
    return render(request, 'home.html', {'sessions': sessions})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def book_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        session.is_booked = True
        session.save()
        return redirect('home')
    return render(request, 'book_session.html', {'session': session})
