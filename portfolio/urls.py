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

    path('guide/', views.guide, name='guide'),
    path('chat/', views.chat, name='chat'),
    path('paylist/', views.paylist, name='paylist'),
]