from django.shortcuts import render, redirect
from .forms import UserForm, MusicForm
from.models import User, AdminUser, Music
from django.contrib.auth import authenticate


# Create your views here.

def home(request):
    music = Music.objects.all()
    musicList = []
    for mus in music:
        musicList.append({'music': mus})

    return render(request, 'home.html', {'musicList': musicList})


def music(request, num):
    music = Music.objects.get(isbn=num)
    music_list = []
    music_list.append({'music': music})

    return render(request, 'music.html', {'music_list': music_list})


def adminpanel(request):
    error = ''
    if request.method == 'POST':
        form = MusicForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            error = 'Posted!!!'
        else:
            error = 'ERROR FORM!!!'

    form = MusicForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'adminpanel.html', data)




def admin(request):
    error = ''
    if request.method == 'POST':
        ema = request.POST.get("email", "Undefined")
        pas = request.POST.get("password", "null")

        if ema != "Undefined" and pas != "null":
            bd = AdminUser.objects.filter(email=ema)
            if bd.exists():
                dat = AdminUser.objects.get(email=ema)
                if ema == dat.email and pas == dat.password:
                    return redirect('/auth/adminpanel/')
                else:
                    error = 'Incorrect data'
            else:
                error = 'AdminUser dont exists, please register'
        else:
            error = 'ERROR'

    data = {'error': error}
    return render(request, 'admin.html', data)


def login(request):
    error = ''
    if request.method == 'POST':
        ema = request.POST.get("email", "Undefined")
        pas = request.POST.get("password", "null")

        if ema != "Undefined" and pas != "null":
            bd = User.objects.filter(email=ema)
            if bd.exists():
                dat = User.objects.get(email=ema)
                if ema == dat.email and pas == dat.password:
                    return redirect('/auth/home')
                else:
                    error = 'Incorrect data'
            else:
                error = 'User dont exists, please register'
        else:
            error = 'ERROR'

    data = {'error': error}
    return render(request, 'login.html', data)


def register(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['email']
            bd = User.objects.filter(email=subject)
            if not bd.exists():
                form.save()
                return redirect('/auth/login')
            else:
                error = 'Пользователь существует'
        else:
            error = 'ERROR FORM'

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'register.html', data)
