from django.shortcuts import render, redirect
from .forms import UserForm, MusicForm
from.models import User, AdminUser, Music
from django.contrib.auth import authenticate
import re

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
                    error = 'Login or password is wrong'
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
            ag = form.cleaned_data['age']
            pas = form.cleaned_data['password']
            bd = User.objects.filter(email=subject)
            x = re.findall("[A-Z]", pas)
            y = re.findall("[a-z]", pas)


            isAge = isinstance(ag,int)
            print(isAge)
            print(type(ag))
            if not bd.exists() and len(pas) >= 8 and x and y:

                form.save()
                return redirect('/auth/login')
            if bd.exists():
                error = 'Пользователь с таким email уже существует'
            elif len(pas) < 8 or not x or not y:
                error += 'Пароль должен содержать больше 8 символов среди которых 1 символ в верхнем и 1 символ в нижних регистрах'
        else:
            error = 'ERROR FORM, проверьте правильность заполненных данных '

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'register.html', data)
