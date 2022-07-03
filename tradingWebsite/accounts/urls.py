from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_user, name='login'),

    path('logout/', LogoutView.as_view(next_page='front_page'), name='logout'),

    path('sign_up/', views.sign_up, name='sign_up'),

    path('delete_user/', views.delete_user, name='delete_user'),

]
