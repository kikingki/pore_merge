from django.urls import path
from user import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('tip/', views.tip, name='tip'),
    path('free/', views.free, name='free'),
    path('signupend/', views.signupend, name='signupend')
]