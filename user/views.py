from django.contrib import auth
from django.shortcuts import render, redirect

from .models import CustomUser, Field
from portfolio.models import Portfolio

from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def main(request):
    portfolios = Portfolio.objects.order_by('-pf_date')     # 최신순 정렬
    fields = Field.objects.all()
    return render(request, 'user/main.html', {'portfolios':portfolios, 'fields':fields})

def withdraw(request):
    return render(request, 'user/withdraw.html')

#가입할 때 username, name, pw, nickname, account입력받게하고 cr_id랑 field_id는 어드민에 넣어서 입력 받게 했어요
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            name = form.cleaned_data['name'],
            password = form.cleaned_data['password'],
            nickname = form.cleaned_data['nickname'],
            account = form.cleaned_data['account'],
            cr_id = form.cleaned_data['cr_id'],
            field_id = form.cleaned_data['field_id'])
            auth.login(request, new_user)
            #가입되면 가입완료로 이동
            return redirect('signupend')
    else:
        #아니면 signup으로 가기
        form = UserForm()
        return render(request, 'user/signup.html', {'form':form})

def signupend(request):
    return render(request, 'user/signupend.html')

# login -> signin 변경
def signin(request):
    #로그인이 되면 main으로
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           new_user = form.get_user()
           auth.login(request, new_user)
           return redirect('main')   
        else:
            return render(request, 'user/signin.html', {'form':form})
    else:
        #로그인이 안되면 다시 로그인하도록..!!
        form = AuthenticationForm()
        return render(request, 'user/signin.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main')

def tip(request):
    return render(request, 'user/tip.html')

def free(request):
    return render(request, 'user/free.html')