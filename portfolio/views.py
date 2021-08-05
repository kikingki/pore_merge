from os import error, stat
from django.db.models import fields
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator

# 결제
import requests

from user.models import Career
from .models import CustomUser, Portfolio, Field, Business
from .forms import PortfolioForm, CheckPasswordForm, ProfileForm, BusinessForm, InfoChangeForm



def pfshow(request, field_id):
    portfolios = Portfolio.objects.all()
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'portfolio/pfshow.html', {'field':field,'portfolios':portfolios})

def mypage(request):
    # 로그인 상태가 아닐 경우 signin 페이지 이동
    if not request.user.is_active:
        return render(request, 'user/signin.html')

    # 현재 로그인한 유저
    user = request.user
    portfolios = Portfolio.objects.filter(user_id=user).order_by('-pf_date')
    paginator = Paginator(portfolios, 4)
    page = request.GET.get('page')
    portfolios = paginator.get_page(page)
    business  = Business.objects.all()

    # 등급 구현
    pay = Business.objects.filter(status = "paid").filter(u_id = user)
    grade = ""
    top = ""
    if pay.count() > 2 and pay.count() < 7:
        grade = "2"
        user.cr_id = Career.objects.get(user_ap = "전문가")
        user.save()
    elif pay.count() > 6:
        grade = ""
        top = "3"
    return render(request, 'portfolio/mypage.html', {'portfolios':portfolios,'business':business, 'grade':grade, 'top':top})

# 프로필 추가
def profile_add(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('mypage')
    else:
        form = ProfileForm()
        return render(request, 'portfolio/profile_update.html', {'form':form})

# 프로필 수정
def profile_update(request, id):
    # 로그인 user의 id 값을 받아 해당 유저의 profile 변수 생성
    user = get_object_or_404(CustomUser, id=id)
    profile = user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        info = InfoChangeForm(request.POST, instance=user)
        if form.is_valid() and info.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            info.save()
            return redirect('mypage')
    else:
        form = ProfileForm(instance=profile)
        info = InfoChangeForm(instance=user)
        return render(request, 'portfolio/profile_update.html', {'form':form, 'info':info})


def userpage(request, id):
        # 해당 포트폴리오를 올린 유저 정보
        user = get_object_or_404(CustomUser, id=id)
        portfolios = Portfolio.objects.filter(user_id=user).order_by('-pf_date')
        paginator = Paginator(portfolios, 4)
        page = request.GET.get('page')
        portfolios = paginator.get_page(page)
        business  = Business.objects.all()

        # 등급 구현
        pay = Business.objects.filter(status = "paid").filter(u_id = user)
        grade = ""
        top = ""
        if pay.count() > 2 and pay.count() < 7:
            grade = "2"
            user.cr_id = Career.objects.get(user_ap = "전문가")
            user.save()
        elif pay.count() > 6:
            grade = ""
            top = "3"
        return render(request, 'portfolio/userpage.html', {'portfolios':portfolios, 'user':user,'business':business, 'grade':grade, 'top':top})

def guide(request):
    return render(request, 'portfolio/guide.html')

# 포트폴리오 업로드
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

# 포트폴리오 수정
def pfedit(request, id):
    pf = get_object_or_404(Portfolio, id=id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=pf)
        if form.is_valid():
            pf = form.save(commit=False)
            pf.pf_date = timezone.now()
            pf.save()
            return redirect('pfdetail', id)
    else:
        form = PortfolioForm(instance=pf)
        return render(request, 'portfolio/pfedit.html', {'form':form})

# 포트폴리오 삭제
def delete(request, id):
    pf = get_object_or_404(Portfolio, id=id)
    pf.delete()
    return redirect('mypage')

# 포트폴리오 상세
def pfdetail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'portfolio/pfdetail.html', {'portfolio':portfolio})
    
# 회원 탈퇴
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

# 결제 내역
def paylist(request):
    pay = Business.objects.filter(status = "paid")  # 결제 완료인 Business 모델만 가져옴.
    return render(request, 'portfolio/paylist.html', {'pay':pay})


# 게시글 업로드
def dealupload(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.deal_date = timezone.now()
            deal.u_id = request.user
            deal.field_id = request.user.field_id
            deal.save()
            return redirect('mypage')
    else:
        form = BusinessForm()
        return render(request, 'portfolio/deal_upload.html', {'form':form})

# 게시글 수정
def dealedit(request, id):
    deal = get_object_or_404(Business, id=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=deal)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.deal_date = timezone.now()
            deal.save()
            return redirect('dealdetail', id)
    else:
        form = BusinessForm(instance=deal)
        return render(request, 'portfolio/deal_edit.html', {'form':form})

# 게시글 삭제
def dealdelete(request, id):
    deal = get_object_or_404(Business, id=id)
    deal.delete()
    return redirect('mypage')

# 게시글 상세
def dealdetail(request, id):
    deal = get_object_or_404(Business, id=id)
    return render(request, 'portfolio/deal_detail.html', {'deal':deal})
    


# 카카오 페이
def kakaoPay(request, id):
    deal = get_object_or_404(Business, id=id)
    return render(request, 'portfolio/kakaopay.html', {'deal':deal})

def kakaoPayLogic(request, id):
    deal = get_object_or_404(Business, id=id)
    _admin_key = 'e721c22025f81af8cf73973e9d3b7402' # 입력필요
    _url = f'https://kapi.kakao.com/v1/payment/ready'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
    }
    _data = {
        'cid': 'TC0ONETIME',
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'item_name':deal.deal_title,
        'quantity':'1',
        'total_amount':deal.price,
        'vat_amount':'0',
        'tax_free_amount':'0',
        # 내 애플리케이션 -> 앱설정 / 플랫폼 - WEB 사이트 도메인에 등록된 정보만 가능합니다
        # * 등록 : http://IP:8000 
        'approval_url':'http://127.0.0.1:8000/portfolio/paySuccess', 
        'fail_url':'http://127.0.0.1:8000/portfolio/payFail',
        'cancel_url':'http://127.0.0.1:8000/portfolio/payCancel'
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    request.session['tid'] = _result['tid']
    return redirect(_result['next_redirect_pc_url'])

def paySuccess(request):
    _url = 'https://kapi.kakao.com/v1/payment/approve'
    _admin_key = 'e721c22025f81af8cf73973e9d3b7402' # 입력필요
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
    _data = {
        'cid':'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'pg_token': request.GET['pg_token']
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    if _result.get('msg'):
        return redirect('payFail')
    else:
        return render(request, 'portfolio/paySuccess.html')

def payFail(request):
    return render(request, 'portfolio/payFail.html')

def payCancel(request):
    return render(request, 'portfolio/payCancel.html')