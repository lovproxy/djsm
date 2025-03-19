from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import xd,xd2,xd3,xd4
from .models import Entry
from .forms import StihForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
   ListView,
   DetailView,
)


def ocn(requests):
    return render(requests, 'glav.html')

def stixi(requests):
    return render(requests,'katal.html')


def st5(requests):
    entries = Entry.objects.all().order_by('-datepublic')
    return render(requests, 'st5.html', {'entries': entries})



def lec(requests):
    txt = xd.objects.filter()[:5]
    return render(requests, 'st1.html',{'txt':txt})



def open(requests):
    ttt = xd.objects.filter()[5:]
    return render(requests,'st11.html',{'ttt':ttt})


def love(requests):
    txt2 = xd2.objects.filter()[:5]
    return render(requests, 'st2.html', {'txt2': txt2})

def open2(requests):
    ttt2 = xd2.objects.filter()[5:]
    return render(requests, 'st21.html', {'ttt2': ttt2})

def fil(requests):
    txt3 = xd3.objects.filter()[:5]
    return render(requests, 'st3.html', {'txt3': txt3})

def open3(requests):
    ttt3 = xd3.objects.filter()[5:]
    return render(requests, 'st31.html', {'ttt3': ttt3})



def grazhd(requests):
    txt4 = xd4.objects.filter()
    return render(requests, 'st4.html', {'txt4': txt4})




class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("id")


def index(request):
    if request.method == 'POST':
        form = StihForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Cпасибо за публикацию.")
            return HttpResponseRedirect('/admin/dj/entry/')
    else:
        form = StihForm()
    return render(request, 'form.html', {'form': form})


@login_required
def stih_form(request):
    if request.method == 'POST':
        form = StihForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            print(f"Сохранено новое произведение: {entry.title} от {entry.author}")
            messages.success(request, f'Произведение "{entry.title}" успешно добавлено!')
            return HttpResponseRedirect(f'/profile/{request.user.id}/')
        else:
            print("Ошибки формы:", form.errors)
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = StihForm()
    return render(request, 'form.html', {'form': form})

@login_required
def profile(request, user_id):
    # Получаем пользователя профиля
    profile_user = get_object_or_404(User, id=user_id)
    
    # Проверяем, является ли текущий пользователь владельцем профиля
    is_owner = request.user.id == profile_user.id
    
    # Получаем записи пользователя
    entries = Entry.objects.filter(user=profile_user).order_by('-datepublic')
    print(f"Найдено произведений пользователя {profile_user.username}: {entries.count()}")
    for entry in entries:
        print(f"Произведение: {entry.title} от {entry.author}")
    
    return render(request, 'profile.html', {
        'entries': entries,
        'profile_user': profile_user,
        'is_owner': is_owner
    })

@login_required
def my_profile(request):
    print(f"DEBUG: Перенаправление на профиль пользователя {request.user.id}")
    return HttpResponseRedirect(f'/profile/{request.user.id}/')



