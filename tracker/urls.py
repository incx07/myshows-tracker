from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('search/', views.search, name='search_list'),
    path('<int:id>/', views.detail, name='detail'),
    path('accounts/register/', views.MyRegisterFormView.as_view(), name="register"),
]
