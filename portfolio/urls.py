from django.urls import path,include
from portfolio import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('guide/', views.guide, name='guide'),
    path('pfupload/', views.pfupload, name='pfupload'),
    path('pfdetail/<int:id>/', views.pfdetail, name='pfdetail'),
    path('pfedit/<int:id>/', views.pfedit, name='pfedit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('chat/', views.chat, name='chat'),
    path('paylist/', views.paylist, name='paylist'),
    path('pfshow/<int:field_id>', views.pfshow, name='pfshow'),
]