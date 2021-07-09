from django.db import models
# user 앱에서 CustomUser, Field 모델 import
from user.models import CustomUser, Field
from django.db.models import fields 

class Portfolio(models.Model):
    def __str__(self):
        return self.pf_title

    pf_title = models.CharField(max_length=200)
    pf_content = models.TextField()
    pf_attach = models.FileField(blank=True, upload_to="images/", null=True)    # summernote 쓰면 필요할까?
    pf_date = models.DateTimeField()

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='portfolios', null=True)    # 글 작성자
    f_id = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='portfolios', null=True)            # 포트폴리오 분야