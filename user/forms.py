from django import forms
from django.db import models
from django.forms import fields
from .models import CustomUser


#model에 넣은대로 입력되게 했어요
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'password', 'nickname', 'account', 'cr_id', 'field_id']
        # 회원가입에 필드 이름 대신 띄우는 문자열
        labels = {
            'username': '아이디',
            'name': '이름',
            'password': '비밀번호',
            'nickname': '닉네임',
            'account': '계좌번호',
            'cr_id': '경력',
            'field_id': '직업'
        }
