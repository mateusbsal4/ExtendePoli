from django.urls import path

from . import views

app_name = 'equipes'
urlpatterns = [
    path('', views.list_equipes, name='index'), # adicione esta linha
    path('create/', views.create_equipe, name='create'),
    path('<int:equipe_id>/', views.detail_equipe, name='detail'),
    path('update/<int:equipe_id>/', views.update_equipe, name='update'),
    path('delete/<int:equipe_id>/', views.delete_equipe, name='delete'),
    path('<int:equipe_id>/membro/', views.create_membro, name='membro'),
    path('<int:membro_id>/delete_membro/', views.delete_membro, name='delete-membro'),
    path('<int:equipe_id>/foto/', views.create_foto, name='foto'),
    path('<int:foto_id>/delete_foto/', views.delete_foto, name='delete-foto'),
    path('<int:equipe_id>/evento/', views.edit_evento, name='evento'),

]   
