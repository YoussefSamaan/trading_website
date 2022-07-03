from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
]
