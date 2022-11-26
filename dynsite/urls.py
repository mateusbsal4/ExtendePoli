from django.urls import path

from . import views

app_name = 'dynsite'
urlpatterns = [
    path('', views.list_equipes, name='index'), # adicione esta linha
    path('<str:equipe_nome>/', views.detail_equipe, name='detail'),
]