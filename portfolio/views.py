from os import error
from django.db.models import fields
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import CustomUser, Portfolio, Field
from .forms import PortfolioForm, CheckPasswordForm



def pfshow(request, field_id):
    portfolios = Portfolio.objects.all()
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'portfolio/pfshow.html', {'field':field,'portfolios':portfolios})

def mypage(request):
    # 로그인 상태가 아닐 경우 signin 페이지 이동
    if not request.user.is_active:
        return render(request, 'user/signin.html')

    portfolios = Portfolio.objects.all()
    # 현재 로그인한 유저
    user = request.user
    return render(request, 'portfolio/mypage.html', {'portfolios':portfolios})

def userpage(request, id):
        portfolios = Portfolio.objects.all()
    # 현재 로그인한 유저
        user = get_object_or_404(CustomUser, id=id)
        return render(request, 'portfolio/userpage.html', {'portfolios':portfolios, 'user':user})

def guide(request):
    return render(request, 'portfolio/guide.html')

def pfupload(request):
    if not request.user.is_active:
        return render(request, 'user/signin.html')

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            pf = form.save(commit=False)
            pf.pf_date = timezone.now()
            pf.user_id = request.user
            pf.f_id = request.user.field_id
            pf.save()
            return redirect('mypage')
    else:
        form = PortfolioForm()
        return render(request, 'portfolio/pfupload.html', {'form':form})

def pfedit(request, id):
    pf = get_object_or_404(Portfolio, id=id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=pf)
        if form.is_valid():
            pf = form.save(commit=False)
            pf.pf_date = timezone.now()
            pf.save()
            return redirect('pfdetail', id)
    else:
        form = PortfolioForm(instance=pf)
        return render(request, 'portfolio/pfedit.html', {'form':form})

def delete(request, id):
    pf = get_object_or_404(Portfolio, id=id)
    pf.delete()
    return redirect('mypage')


def pfdetail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'portfolio/pfdetail.html', {'portfolio':portfolio})
    
def withdraw(request):
    return render(request, 'portfolio/withdraw.html')

def user_delete(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            return redirect('main')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'portfolio/user_del.html', {'password_form':password_form})


def chat(request):
    return render(request, 'portfolio/chat.html')

def paylist(request):
    return render(request, 'portfolio/paylist.html')
