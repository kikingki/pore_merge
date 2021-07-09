from django import forms
from django.db.models import fields
from .models import Portfolio

from django_summernote.widgets import SummernoteWidget

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['pf_title', 'pf_content', 'pf_attach']

        # pf_content의 위젯으로 summernote 사용
        widgets = {
            'pf_content': SummernoteWidget(),
        }

        labels = {
            'pf_title': '제목',
            'pf_content': '내용',
            'pf_attach': '첨부파일',
        }