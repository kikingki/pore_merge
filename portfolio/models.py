from django.db import models
# user 앱에서 CustomUser, Field 모델 import
from user.models import CustomUser, Field
from django.db.models import fields 

class Portfolio(models.Model):
    def __str__(self):
        return self.pf_title

    pf_title = models.CharField(max_length=200)
    pf_content = models.TextField()
    pf_attach = models.ImageField(blank=True, upload_to="images/", null=True)    # 썸네일
    pf_date = models.DateTimeField()

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='portfolios', null=True)    # 글 작성자
    f_id = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='portfolios', null=True)            # 포트폴리오 분야


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField(blank=True, upload_to="images/", null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    introduce = models.TextField(null=True, blank=True)


class Business(models.Model):
    def __str__(self):
        return self.deal_title
        
    deal_title = models.CharField(max_length=200)
    deal_content = models.TextField()
    deal_date = models.DateTimeField()
    u_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='business', null=True)
    price = models.CharField(max_length=200)
    status = models.CharField(
        max_length=9,
        choices=(
            ('ready', '미결제'),
            ('paid', '결제완료'),
        ),
        default='ready',
        db_index=True)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='business', null=True)