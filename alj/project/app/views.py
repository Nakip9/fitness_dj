from django.shortcuts import render, redirect, get_object_or_404
from .models import Session
from .forms import RegisterForm
from django.contrib.auth import login


def home(request):
    sessions = Session.objects.select_related('user').order_by('session_date')
    next_session = sessions.filter(is_booked=False).first()
    context = {
        'sessions': sessions,
        'next_session': next_session,
    }
    return render(request, 'home.html', context)


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
    if request.method == 'POST' and not session.is_booked:
        session.is_booked = True
        session.save()
        return redirect('home')
    return render(request, 'book_session.html', {'session': session})
