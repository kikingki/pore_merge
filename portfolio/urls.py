from django.urls import path,include
from portfolio import views

urlpatterns = [
    # 마이페이지
    path('', views.mypage, name='mypage'),
    path('profile_add/', views.profile_add, name='profile_add'),
    path('profile_update/<int:id>', views.profile_update, name='profile_update'),
    path('userpage/<int:id>/', views.userpage, name='userpage'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('withdraw/delete/', views.user_delete, name='user_del'),

    # 포트폴리오
    path('pfupload/', views.pfupload, name='pfupload'),
    path('pfshow/<int:field_id>', views.pfshow, name='pfshow'),
    path('pfdetail/<int:id>/', views.pfdetail, name='pfdetail'),
    path('pfedit/<int:id>/', views.pfedit, name='pfedit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    # 거래글
    path('dealupload/', views.dealupload, name='dealupload'),
    path('dealdetail/<int:id>/', views.dealdetail, name='dealdetail'),
    path('dealedit/<int:id>/', views.dealedit, name='dealedit'),
    path('dealdelete/<int:id>/', views.dealdelete, name='dealdelete'),

    # 카카오페이
    path('kakaoPay/<int:id>/', views.kakaoPay, name='kakaoPay'),                 #결제 페이지(버튼)
    path('kakaoPayLogic/<int:id>/', views.kakaoPayLogic, name='kakaoPayLogic'),  #결제 처리 주소
    path('paySuccess/', views.paySuccess, name='paySuccess'),           # 결제 완료
    path('payFail/', views.payFail, name='payFail'),                    # 결제 오류
    path('payCancel/', views.payCancel, name='payCancel'),    

    path('guide/', views.guide, name='guide'),
    path('chat/', views.chat, name='chat'),
    path('paylist/', views.paylist, name='paylist'),
]