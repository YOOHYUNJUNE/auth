from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    # 회원가입시 바로 로그인 창 
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form =CustomUserCreationForm(request.POST)
        if form.is_valid(): # 비번 confirm까지 됐을때 / 잘못 제출시 context로 이동
            user = form.save()
            auth_login(request, user) # 가입시 바로 로그인
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'account_form.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            # 단축평가 / A or B : A = True, B 상관없이 A / A = False, B
            next_url = request.GET.get('next') # articles/create
            # return redirect('accounts:login')
            return redirect(next_url or 'articles:index')
            # next인자가 url에 있을때 : '/articles/create' or 'articles:index'
            # next인자가 url에 없을때 : None or 'articles:index'

    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'account_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')